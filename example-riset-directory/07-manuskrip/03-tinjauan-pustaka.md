# Tinjauan Pustaka

## 2.1. SMS Spam dan Tantangan Bahasa Indonesia
[cite_start]SMS spam merupakan gangguan komunikasi yang tidak diinginkan, mencakup iklan ilegal, modus penipuan finansial, dan konten phishing[cite: 29, 31]. [cite_start]Karakteristik bahasa Indonesia yang tidak baku dan penggunaan singkatan gaul menjadi tantangan utama dalam klasifikasi teks[cite: 45].

## 2.2. Algoritma Klasifikasi
* [cite_start]**Naïve Bayes (Baseline/Kondisi A):** Algoritma berbasis probabilitas yang sering digunakan sebagai *benchmark* karena efisiensi komputasinya yang tinggi dalam pemrosesan teks[cite: 41, 44].
* [cite_start]**Support Vector Machine (Intervensi/Kondisi B):** Algoritma yang mencari *hyperplane* pembatas dengan margin maksimal, sangat efektif untuk menangani dimensi fitur yang tinggi pada data teks[cite: 39, 40].

## 2.3. Penelitian Terkait (State of the Art)
[cite_start]Penelitian terdahulu oleh Widyawati & Susanto (2019) menunjukkan efektivitas Naïve Bayes pada teks SMS [cite: 44, 116][cite_start], sementara Sofyan dkk (2024) membuktikan kekuatan SVM dalam memisahkan teks normal dan spam[cite: 45, 115]. [cite_start]Namun, riset ini mengisi celah (gap) dengan melakukan perbandingan langsung (head-to-head) yang adil menggunakan dataset yang identik, untuk membuktikan secara empiris apakah intervensi SVM benar-benar memberikan peningkatan performa yang signifikan dibandingkan baseline Naïve Bayes[cite: 48, 49].