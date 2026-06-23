# Proposal Riset Teknologi Informasi
**Universitas Putra Bangsa (UPB) Kebumen**
**Tahun Akademik: 2026**

---

## Data Mahasiswa
* **Nama / NIM:** Ismi Nur Fadilah (240202868)
* **Program Studi:** Ilmu Komputer
* **Fakultas:** Sains dan Teknologi

---

## A. Judul Penelitian
**Analisis Komparatif Algoritma Support Vector Machine dan Naïve Bayes untuk Klasifikasi Teks SMS Spam Berbahasa Indonesia**

## B. Ringkasan Proyek
Penelitian ini bertujuan untuk mengukur, menganalisis, dan membuktikan secara empiris akurasi klasifikasi teks biner dalam menyaring SMS spam berbahasa Indonesia menggunakan pendekatan *Machine Learning*. Eksperimen dilakukan secara objektif memanfaatkan dataset publik sekunder berisikan 1.623 baris data teks pesan SMS berbahasa Indonesia (repositori Yudi Wibisono) dengan proporsi pembagian data latih dan data uji sebesar 80:20 dengan penguncian acak `random_state=42`. Kinerja kedua model divalidasi menggunakan instrumen *Confusion Matrix* ke dalam metrik kuantitatif: Akurasi, Precision, dan Recall.

**Kata Kunci:** SMS Spam; Support Vector Machine; Naive Bayes; Analisis Komparatif; TF-IDF

---

## C. Pendahuluan & Rumusan Masalah

### C.1 Latar Belakang dan Masalah
Karakteristik infrastruktur komunikasi Short Message Service (SMS) di Indonesia yang bersifat terbuka disalahgunakan oleh pihak tidak bertanggung jawab untuk menyebarkan pesan gangguan (*spam*) secara massal (iklan massal ilegal, judi online, info hadiah palsu, hingga scam penipuan finansial). Dampak langsungnya meliputi terganggunya kenyamanan komunikasi digital, tingginya risiko kebocoran data pribadi akibat tautan *phishing*, hingga kerugian materi akibat pinjaman online ilegal. 

**Rumusan Masalah:** Bagaimana merancang sebuah pemodelan klasifikasi biner cerdas menggunakan pendekatan *supervised learning* yang mampu membedakan teks normal (*ham*) dan teks gangguan (*spam*) secara presisi berdasarkan karakteristik sebaran kata di Indonesia?

### C.2 Celah Riset (Gap Utama) & Hipotesis
* **Celah Riset:** Belum ada penelitian lokal yang membandingkan secara langsung performa SVM (Intervensi) melawan Naïve Bayes (Baseline) secara adil menggunakan data mentah dan urutan sistem pembersihan teks (*preprocessing*) yang benar-benar identik pada dataset pesan pendek Indonesia berskala 1.623 data.
* **Research Question (RQ):** Apakah metode *Support Vector Machine* menghasilkan performa yang lebih baik dibandingkan Naïve Bayes dalam klasifikasi SMS spam berbahasa Indonesia berdasarkan metrik akurasi, precision, dan recall?
* **Hipotesis Alternatif ($H_1$):** Terdapat perbedaan performa yang signifikan antara penggunaan algoritma *Support Vector Machine* (SVM) dan algoritma Naïve Bayes (NB) dalam mengklasifikasikan pesan SMS ke dalam label spam atau normal.

---

## D. Metodologi Eksperimen (Skenario Pengujian)

Eksperimen laboratorium ini dirancang menggunakan logika pembandingan sejajar yang adil (*fairness checklist*) di bawah lingkungan **Python 3.13.7** dengan prosedur:

1. **Pemuatan Data:** Dataset 1.623 baris SMS dimuat ke dalam *environment*. Label normal diubah menjadi kelas `0` dan spam menjadi kelas `1`.
2. **Pembersihan Teks Tegas (Pipeline Preprocessing):** Seluruh data diproses melewati alur *case folding*, *tokenizing* (pembuangan simbol/angka), *stopword removal*, dan pemotongan imbuhan (*stemming*) menggunakan pustaka `Sastrawi==1.0.1`.
3. **Ekstraksi Fitur:** Representasi teks diubah menjadi matriks angka menggunakan pembobotan *Term Frequency-Inverse Document Frequency* (TF-IDF Vectorizer).
4. **Pemisahan Data:** Data dipisahkan dengan proporsi tetap 80% data latih dan 20% data uji (`random_state=42`).
5. **Skenario Komparasi:**
   * **Skenario A (Baseline):** Data dilatih menggunakan algoritma klasik *Multinomial Naïve Bayes*.
   * **Skenario B (Intervensi Utama):** Data dilatih menggunakan algoritma *Support Vector Machine* dengan kernel RBF yang dioptimasi setelan parameternya lewat fungsi `GridSearchCV`.
6. **Validasi:** Kedua model divalidasi silang menggunakan skema *10-Fold Cross-Validation*.

---

## E. Luaran Artefak Teknis yang Ditargetkan
1. **Tabel Performa Komparatif:** Tabel persentase berdampingan (*Side-by-side Matrix*) untuk membaca selisih angka matematika dari kedua algoritma. Target akurasi model intervensi (SVM) diproyeksikan mampu melampaui 95%.
2. **Artefak Pipeline Komputasi:** Berkas skrip kode program Python utuh (`.ipynb`) yang mencakup otomatisasi dari pra-pemrosesan hingga *tuning* parameter otomatis yang bersifat *reproducible* (bisa dijalankan ulang secara persis).
3. **Dokumen Laporan Akhir:** Analisis mendalam (*Error Analysis Document*) yang memuat visualisasi grafik *Confusion Matrix* terkait karakteristik kata gaul/singkatan Indonesia yang gagal diklasifikasikan oleh model.