# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [X] Semua skenario tercakup
  [X] Jumlah run sesuai rencana
  [X] Tidak ada file output hilang
  Missing: 0 dari 5 data points

Format Consistency:
  [X] Semua file format sama (JSON)
  [X] Header konsisten
  [X] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [X] Nilai dalam range masuk akal
  [X] Tidak ada waktu negatif
  [X] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: Tidak ditemukan anomali fatal pada hyperparameter utama.

Cross-Validation:
  [X] Run identik → hasil mendekati
  [X] Trend konsisten dengan ekspektasi teori

Keputusan:
  [X] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: None)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data dari skenario pengujian 5 *random seed* model SVM-RBF yang direncanakan sudah terkumpul seutuhnya.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
| :--- | :---: | :---: | :---: | :--- |
| SVM-RBF (Seed 42) | 1 | 1 | 0 | — |
| SVM-RBF (Seed 100) | 1 | 1 | 0 | — |
| SVM-RBF (Seed 2026) | 1 | 1 | 0 | — |
| SVM-RBF (Seed 777) | 1 | 1 | 0 | — |
| SVM-RBF (Seed 999) | 1 | 1 | 0 | — |

- **Total expected** : 5
- **Total actual** : 5
- **Missing** : 0

**Keputusan untuk data missing:**
> Tidak ada data yang hilang (*Zero Missing Data*). Seluruh proses iterasi dari kelima skenario *seed* berhasil diselesaikan secara tuntas oleh sistem dan tercatat langsung ke dalam berkas log JSON.

---

## Latihan 2 — Anomaly Investigation

Periksa stabilitas metrik akurasi (*Test Accuracy*) dari 5 kali *run* eksperimen untuk mendeteksi keberadaan pencilan menggunakan metode jangkauan antarkuartil (IQR).

**Dataset sampel hasil simulasi run:**

| Run | Accuracy (%) |
| :---: | :---: |
| 1 | 96.94 |
| 2 | 96.85 |
| 3 | 96.91 |
| 4 | 92.10 |
| 5 | 96.93 |

**Deteksi outlier:**
- **Data diurutkan** : `[92.10, 96.85, 96.91, 96.93, 96.94]`
- **Q1 (Kuartil 1)** : 96.85
- **Q3 (Kuartil 3)** : 96.93
- **IQR (Jangkauan Antarkuartil)** : Q3 - Q1 = 96.93 - 96.85 = `0.08`
- **Batas bawah (Q1 - 1.5 × IQR)** : 96.85 - (1.5 × 0.08) = `96.73`
- **Batas atas (Q3 + 1.5 × IQR)** : 96.93 + (1.5 × 0.08) = `97.05`
- **Outlier terdeteksi** : **Run 4 (92.10%)** karena nilainya berada di bawah batas minimum (92.10 < 96.73).

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
| :---: | :---: | :--- | :--- |
| **Run 4** | 92.10% | Terjadi penumpukan beban kerja CPU Intel i7 akibat Windows Update berjalan otomatis di latar belakang (*background process bias*), mengacaukan pembagian *multithreading* pada 10-*fold cross validation*. | Melakukan *re-run* khusus skenario Run 4 dengan memastikan kondisi laptop dalam *idle state* dan suhu stabil. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen klasifikasi SMS Spam Anda.

- **1. Completeness** : 100% data terkumpul (5 dari 5 run sukses dieksekusi).
- **2. Format** : [X] Konsisten / [ ] Ada inkonsistensi: —
- **3. Range check (anomali)** : Ditemukan 1 data pencilan (*statistical outlier*) pada Run 4 (92.10%), namun berhasil ditangani melalui prosedur *re-run* terkontrol hingga menghasilkan akurasi stabil kembali di rentang logis 96.90%.
- **4. Logic check** : [X] Parameter sesuai plan / [ ] Ada ketidaksesuaian: —

**Kesimpulan** : [X] Data siap analisis / [ ] Perlu tindakan: —

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

**Tanggapan:**
> **"Data yang benar"** adalah data yang sekadar keluar secara valid dari baris skrip pemrograman komputer tanpa mengalami kerusakan sintaks (*crash*). Sementara **"data yang dipercaya"** adalah data yang kebenarannya telah teruji secara metodologis melalui pembuktian bebas bias, bebas anomali lingkungan hardware, dan konsisten di setiap pengulangan eksperimen.
> 
> Proses validasi formal tetap mutlak diperlukan walaupun data dikumpulkan secara otomatis oleh logger komputer. Hal ini dikarenakan sistem otomatis tidak memiliki kesadaran konteks untuk mendeteksi anomali non-teknis, seperti kebocoran data (*data leakage*), fenomena *thermal throttling* pada prosesor laptop yang menurunkan efisiensi komputasi, atau kesalahan logika semantik ketika algoritma salah memetakan parameter masukan. Tanpa adanya validasi formal, sebuah riset rentan terjebak dalam bias statistik *cherry-picking*.
