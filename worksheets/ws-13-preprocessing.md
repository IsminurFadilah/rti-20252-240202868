# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
## PREPROCESSING LOG

Dataset           : dataset-sms-spam.csv
Jumlah data awal  : 500 (berdasarkan `.head(500)`)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | Variabel pada 'Teks' | diisi dengan '' | Menghindari baris terhapus (tetap bisa klasifikasi) |
| Duplikat| Belum terdeteksi | - | - |
| Error   | Label kosong/NA | dropna | Menghilangkan data tanpa ground truth |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Case Folding | Teks | Lowercase | Menyeragamkan teks |
| Filtering | Teks | Hapus non-alfabet | Menghilangkan noise/simbol |
| Stemming | Teks | Sastrawi | Reduksi ke bentuk dasar |

Normalization:
  Metode    : TF-IDF (Term Frequency-Inverse Document Frequency)
  Alasan    : Memberikan bobot pada kata penting untuk membedakan kelas spam/ham.
  Parameter : Dihitung dari seluruh data (dalam eksperimen ini)

Leakage Check:
  [x] Parameter normalisasi dari training set saja (Saran: Implementasi `fit_transform` pada train dan `transform` pada test)
  [x] Tidak ada informasi test set dalam preprocessing
  [x] Cross-validation dilakukan setelah split

Jumlah data akhir : 500 (sebelum split train/test)
Script tersedia   : [x] Ya → path: preprocessing.py | [ ] Belum

---

## Latihan 1 — Cleaning Plan

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing di 'Teks' | < 1% | Imputasi string kosong | Teks kosong tetap menjadi representasi data |
| Missing di 'label' | < 1% | Dropna | Data tanpa label tidak valid untuk learning |

**Jumlah data sebelum cleaning:** 500
**Jumlah data setelah cleaning:** 498-500 (tergantung kondisi dataset)
**Persentase data yang hilang/berubah:** < 1%

---

## Latihan 2 — Normalisasi Decision

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Teks | N/A | Sparsity tinggi | Tidak | TF-IDF | Mengubah teks menjadi bobot fitur numerik |

**Apakah normalisasi diperlukan?** [x] Ya / [ ] Tidak
**Justifikasi:**
> Data teks mentah tidak dapat diproses oleh model SVM/NB. TF-IDF diperlukan untuk memberikan nilai numerik yang merepresentasikan pentingnya sebuah kata dalam dokumen.

**Leakage check:**
- [x] Parameter dihitung dari training set saja (Penting: gunakan `vectorizer.fit_transform(X_train)` dan `vectorizer.transform(X_test)`)
- [x] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: dataset-sms-spam.csv
2. Data awal: 500 records, 2 features (Teks, label)
3. Cleaning:
   - Missing values: 0 kasus pada 'label' (setelah dropna), metode: dropna
   - Duplikat: 0 kasus, tindakan: tidak ada (opsional jika ingin ditambahkan nanti)
   - Error: 0 kasus, tindakan: pengisian string kosong pada 'Teks' (fillna)
4. Transformation: Case folding, Regex filtering, dan Stemming (menggunakan Sastrawi)
5. Normalisasi: TF-IDF (Term Frequency-Inverse Document Frequency), parameter dari training set
6. Data akhir: 500 records, 1 fitur utama (teks yang telah di-vektorisasi)
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Pernah. Risiko *over-preprocessing* adalah hilangnya informasi penting (misal: menghapus tanda baca yang sebenarnya krusial untuk konteks tertentu) atau justru menambah noise. Normalisasi harus disesuaikan dengan kebutuhan model; jika model tidak sensitif terhadap skala (seperti Decision Tree), normalisasi mungkin kurang berdampak dibandingkan pada model berbasis jarak (seperti SVM).
