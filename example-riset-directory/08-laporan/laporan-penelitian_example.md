# Laporan Penelitian

**Judul:** Analisis Komparatif Algoritma Support Vector Machine dan Naïve Bayes untuk Klasifikasi Teks SMS Spam Berbahasa Indonesia
**Peneliti:** Ismi Nur Fadilah (240202868)
**Status Penelitian:** Tahap penyusunan naskah jurnal ([../07-manuskrip/](../07-manuskrip/))  


---

## 1. Ringkasan Eksekutif
Penelitian ini bertujuan untuk melakukan analisis komparatif antara algoritma *Support Vector Machine* (SVM) dan *Naïve Bayes* dalam mengklasifikasikan teks SMS spam berbahasa Indonesia. Masalah inti yang diangkat adalah tingginya prevalensi SMS spam yang mengancam keamanan data pribadi pengguna seluler di Indonesia. Evaluasi dilakukan melalui eksperimen terkontrol pada 1.623 baris dataset SMS, menggunakan metrik akurasi, *precision*, dan *recall*.

**Temuan Utama:**
- SVM dan Naïve Bayes menunjukkan performa kompetitif dengan akurasi rata-rata di atas 90%.
- Perbedaan performa tidak signifikan secara statistik ($p > 0.05$).
- Naïve Bayes lebih efisien secara komputasi, sementara SVM memberikan stabilitas presisi yang lebih tinggi.

---

## 2. Pendahuluan
- **Masalah Inti:** Tingginya prevalensi SMS spam berbahasa Indonesia yang tidak terdeteksi secara otomatis, mengancam privasi dan keamanan pengguna.
- **RQ:** Apakah metode SVM menghasilkan performa yang lebih baik dibandingkan Naïve Bayes dalam klasifikasi SMS spam berdasarkan metrik akurasi, *precision*, dan *recall*?
- **Hipotesis:** Terdapat perbedaan performa yang signifikan (H1: SVM > NB).
- (Detail lengkap: [/07-manuskrip/02-pendahuluan.md](/07-manuskrip/02-pendahuluan.md))

---

## 3. Metodologi
Penelitian menggunakan desain eksperimen laboratorium dengan alur kerja berikut:

1. **Preprocessing:** *Case folding, Tokenizing, Stopword Removal, Stemming (Sastrawi).*
2. **Ekstraksi Fitur:** *Term Frequency-Inverse Document Frequency* (TF-IDF).
3. **Model:**
   - **Baseline (Kondisi A):** Naïve Bayes.
   - **Intervensi (Kondisi B):** SVM (*kernel RBF* + *GridSearchCV*).
4. **Validasi:** 10-*Fold Cross-Validation*.

---

## 4. Hasil Penelitian

| Skenario | Akurasi (mean ± std) | F1-Score (mean ± std) | n |
| :--- | :--- | :--- | :--- |
| **SVM** | 0.94 ± 0.01 | 0.93 ± 0.02 | 10 |
| **Naive Bayes** | 0.93 ± 0.02 | 0.92 ± 0.02 | 10 |

---

## 5. Struktur Direktori Artefak

| Folder | Deskripsi |
| :--- | :--- |
| `/01-proposal/` | Proposal Riset Teknologi Informasi |
| `/03-teori/` | Tinjauan pustaka dan teori pendukung |
| `/04-data/` | Dataset 1.623 baris SMS (Yudi Wibisono) |
| `/05-kode/` | Skrip Python eksperimen dan analisis |
| `/06-output/` | Tabel hasil (csv) dan grafik (png) |
| `/07-manuskrip/` | Draf naskah jurnal (format markdown) |
| `/08-laporan/` | Laporan perkembangan penelitian |

---

## 6. Referensi
- Widyawati, R., & Susanto, A. (2019). Komparasi Kinerja Klasifikasi Naïve Bayes dan Support Vector Machine untuk Penyaringan Teks SMS Bahasa Indonesia.
- Sofyan, M. A., dkk. (2024). Deteksi SMS Spam Berbahasa Indonesia Menggunakan Algoritma Support Vector Machine.
- (Referensi lengkap: [/07-manuskrip/07-daftar-pustaka.md](/07-manuskrip/07-daftar-pustaka.md))

---

## 7. Cara Reproduksi
1. Pastikan lingkungan Python memiliki pustaka `scikit-learn` dan `sastrawi`.
2. Muat dataset dari `/04-data/`.
3. Jalankan skrip eksperimen di `/05-kode/`.
4. Hasil akan tersimpan otomatis di folder `/06-output/`.