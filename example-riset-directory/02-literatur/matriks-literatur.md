# Matriks Studi Literatur Penelitian Terdahulu

**Nama / NIM:** Ismi Nur Fadilah (240202868)  
**Judul Riset:** Analisis Komparatif Algoritma Support Vector Machine dan Naïve Bayes untuk Klasifikasi Teks SMS Spam Berbahasa Indonesia

---

## Tabel Matriks Literatur (State of the Art)

Berikut adalah pemetaan terhadap 4 referensi jurnal ilmiah utama yang menjadi acuan landasan teori dan komparasi dalam eksperimen ini:

| No | Peneliti & Tahun | Judul Paper / Jurnal | Metode yang Digunakan | Hasil Utama & Temuan | Keterbatasan / Limitasi Riset |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Widyawati & Susanto (2019) | Komparasi Kinerja Klasifikasi Naïve Bayes dan Support Vector Machine untuk Penyaringan Teks SMS Bahasa Indonesia | Algoritma *Multinomial Naïve Bayes* tunggal tanpa optimasi parameter luar. | Berhasil melakukan penyaringan SMS spam dengan tingkat akurasi yang cukup baik pada pengujian dasar. | Hanya menguji satu metode secara terisolasi, belum dikombinasikan dengan metode optimasi parameter lain yang lebih kuat. |
| **2** | Muslikah (2021) | Deteksi Teks SMS Spam Berbahasa Indonesia Menggunakan Pendekatan Long Short-Term Memory (LSTM) | Pendekatan *Deep Learning* menggunakan arsitektur *Long Short-Term Memory* (LSTM). | Menghasilkan akurasi klasifikasi yang sangat tinggi, terutama dalam mengenali pola susunan kalimat yang panjang. | Beban komputasi proses pelatihan sangat berat, membutuhkan waktu lama, dan kurang efisien untuk karakteristik data SMS yang cenderung pendek. |
| **3** | Dwiyansaputra & dkk (2021) | Klasifikasi Teks SMS Menggunakan Kombinasi Fitur TF-IDF dan Stochastic Gradient Descent | Ekstraksi fitur statistik TF-IDF yang dikombinasikan dengan pengoptimal *Stochastic Gradient Descent* (SGD). | Terbukti sangat efektif dan cepat dalam mengenali pola kata kunci khusus yang sering muncul pada jenis pesan promo komersial. | Model sering kali mengalami kegagalan deteksi jika dihadapkan pada teks SMS yang didominasi singkatan gaul tak baku atau modifikasi karakter teks acak. |
| **4** | Sofyan & dkk (2024) | Deteksi SMS Spam Berbahasa Indonesia Menggunakan Algoritma Support Vector Machine | Klasifikasi teks memanfaatkan algoritma dasar *Support Vector Machine* (SVM). | Mengonfirmasi bahwa batas keputusan (*hyperplane*) pada SVM sangat kuat memisahkan sebaran dimensi data teks normal dan spam. | Skala baris data sampel yang diuji masih tergolong sedikit dan alur riset belum menerapkan mekanisme pencarian parameter otomatis. |

---

## Kesimpulan Posisi Riset Saat Ini (Analisis Gap)
Berdasarkan keterbatasan dari penelitian-penelitian terdahulu di atas, riset yang dilakukan pada repositori ini mengambil posisi untuk **mengisi celah riset (gap)** tersebut. 

Eksperimen ini menguji langsung **SVM (dengan pencarian parameter otomatis GridSearchCV)** berdampingan melawan **Naïve Bayes sebagai Baseline** menggunakan infrastruktur pembersihan data (*pipeline preprocessing* Sastrawi) yang benar-benar identik dan adil pada dataset terstruktur berskala 1.623 baris data.