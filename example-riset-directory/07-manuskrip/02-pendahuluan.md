# Pendahuluan

## Latar Belakang dan Rumusan Masalah
Dalam konteks pemanfaatan teknologi informasi di sektor telekomunikasi seluler Indonesia, layanan *Short Message Service* (SMS) masih memegang peranan penting karena sifatnya yang asinkron, ekonomis, serta dapat diakses secara merata. Namun, karakteristik infrastruktur komunikasi SMS yang bersifat terbuka disalahgunakan untuk menyebarkan pesan gangguan (*spam*) secara massal. [cite_start]**Masalah inti dalam penelitian ini adalah tingginya prevalensi SMS spam berbahasa Indonesia yang tidak terdeteksi secara otomatis, sehingga mengancam privasi dan keamanan data pengguna seluler.** 

Dampak tersebut meliputi terganggunya kenyamanan komunikasi, risiko kebocoran data pribadi akibat *phishing*, hingga kerugian finansial. Oleh karena itu, penelitian ini berfokus pada perancangan pemodelan klasifikasi biner cerdas menggunakan *supervised learning* untuk membedakan teks normal (*ham*) dan teks gangguan (*spam*) secara presisi.

## Pendekatan Pemecahan Masalah
Tujuan utama penelitian ini adalah mengukur dan membuktikan secara empiris tingkat akurasi pemodelan klasifikasi teks biner dalam menyaring SMS spam.

* [cite_start]**Research Question (RQ):** "Apakah metode *Support Vector Machine* (SVM) menghasilkan performa yang lebih baik dibandingkan *Naïve Bayes* dalam klasifikasi SMS spam berbahasa Indonesia berdasarkan metrik akurasi, *precision*, dan *recall*?" 
* [cite_start]**Hipotesis ($H_1$):** Terdapat perbedaan performa yang signifikan antara algoritma *Support Vector Machine* (SVM) dan *Naïve Bayes* dalam mengklasifikasikan SMS spam, di mana SVM menghasilkan skor akurasi yang lebih tinggi secara statistik dibandingkan *Naïve Bayes*. 

**Definisi Variabel Penelitian:**
* **Variabel Independen (IV):** Algoritma klasifikasi, dengan **Baseline (Kondisi A)** menggunakan *Naïve Bayes* berbasis probabilitas kata, dan **Intervensi (Kondisi B)** menggunakan *Support Vector Machine* (SVM) dengan optimasi kernel RBF. 
* [cite_start]**Variabel Dependen (DV):** Performa klasifikasi teks, diukur melalui metrik **Akurasi** (ketepatan prediksi), **Precision** (akurasi deteksi spam), dan **Recall** (sensitivitas penyaringan). 

## State of the Art dan Kebaruan

| Peneliti & Tahun | Metode yang Dipakai | Hasil Utama Penelitian | Keterbatasan (Limitasi) |
| :--- | :--- | :--- | :--- |
| Widyawati & Susanto (2019) | Naive Bayes tunggal | Akurasi cukup baik | Hanya satu metode, belum dibandingkan |
| Muslikah (2021) | Deep Learning (LSTM) | Akurasi tinggi (kalimat panjang) | Proses berat, kurang cocok untuk SMS pendek |
| Dwiyansaputra dkk (2021) | TF-IDF + Stochastic Gradient | Efektif mengenali kata kunci | Sering salah tebak singkatan gaul |
| Sofyan dkk (2024) | Support Vector Machine | Sangat kuat memisahkan spam | Data sedikit, belum ada setelan parameter otomatis |

**Pola Teridentifikasi & Analisis Gap:**
* **Kondisi Aktual:** Riset cenderung terisolasi pada satu algoritma.
* **Kondisi Ideal:** Perbandingan adil (*head-to-head*) dengan urutan *preprocessing* yang identik.
* **Celah Riset (Gap):** Perbandingan performa SVM (Intervensi) vs Naive Bayes (Baseline) pada dataset pesan pendek Indonesia berskala 1.623 data.

## Peta Jalan Penelitian
Peta jalan penelitian ini mencakup tiga tahapan:
1. [cite_start]**Tahap Inisiasi (Telah Dicapai):** Studi literatur *concept-centric*, formulasi masalah, dan eksplorasi data menggunakan dataset 1.623 SMS dari repositori Yudi Wibisono. 
2. [cite_start]**Tahap Eksekusi (Usulan Ini):** Eksperimen laboratorium melalui arsitektur pembersihan teks (*case folding, tokenizing, stopword removal, stemming*) serta pengujian model menggunakan 10-Fold Cross-Validation. 
3. [cite_start]**Tahap Analisis:** Bedah pola kesalahan klasifikasi (*False Positive/Negative*) untuk mengidentifikasi karakteristik kata gaul baru yang memengaruhi batas keputusan algoritma. 

---
*Catatan: **Populasi** penelitian ini adalah seluruh data pesan teks SMS berbahasa Indonesia. **Sampel** diambil sebanyak 1.623 baris data menggunakan teknik **purposive sampling** (data sekunder) dengan **kriteria inklusi** berupa pesan SMS berbahasa Indonesia berlabel biner dan **kriteria eksklusi** berupa pesan bahasa asing/tanpa label.*