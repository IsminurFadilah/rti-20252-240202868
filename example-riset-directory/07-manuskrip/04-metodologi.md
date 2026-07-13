# Metodologi

## Desain Penelitian dan Unit Analisis

| Komponen Eksperimen | Penjelasan |
| :--- | :--- |
| **Jenis & Desain** | Pendekatan kuantitatif positivis dengan metode eksperimen laboratorium (*controlled experiment*) berupa studi perbandingan sejajar (*comparison study*). |
| **Unit Analisis (Objek)** | Dokumen teks pendek berupa baris pesan SMS tunggal berbahasa Indonesia. |
| **Konteks Penelitian** | Penyaringan pesan teks lokal yang mengandung kata tidak baku, singkatan acak, iklan massal, atau penipuan. |
| **RQ Final** | Apakah metode *Support Vector Machine* (SVM) menghasilkan performa yang lebih baik dibandingkan *Naïve Bayes* dalam klasifikasi SMS spam berbahasa Indonesia berdasarkan metrik akurasi, *precision*, dan *recall*? |
| **Hipotesis Kerja** | **(H0):** Tidak ada perbedaan performa yang signifikan antara kedua model. **(H1):** Algoritma SVM menghasilkan performa klasifikasi yang lebih tinggi dan signifikan dibanding *Naïve Bayes*. |
| **Baseline (Kondisi A)** | Algoritma *Naïve Bayes* berbasis probabilitas kata (mewakili praktik umum saat ini). |
| **Intervensi (Kondisi B)** | *Support Vector Machine* (SVM) dengan optimasi parameter otomatis lewat *GridSearchCV*. |

**Populasi dan Sampel:**
* **Populasi:** Seluruh data pesan teks SMS berbahasa Indonesia.
* **Sampel:** 1.623 baris data teks menggunakan teknik *purposive sampling* (data sekunder terlabeli).
* **Kriteria:** Inklusi (pesan SMS berbahasa Indonesia berlabel biner), Eksklusi (pesan asing atau tanpa label).

## Variabel, Metric, Instrumen, dan Data
1. **Variabel Penelitian:**
    * **Variabel Independen (IV):** Jenis algoritma klasifikasi, yaitu SVM (intervensi) dan *Naïve Bayes* (baseline).
    * **Variabel Dependen (DV):** Tingkat performa klasifikasi (Akurasi, *Precision*, *Recall*).
    * **Variabel Kontrol:** Pipeline *text preprocessing*, skema TF-IDF, serta proporsi data latih (80%) dan uji (20%).
2. **Metrik:** Akurasi, *Precision*, dan *Recall* (skala rasio 0-100%).
3. **Instrumen:** Pustaka Scikit-Learn (*classification_report* dan *confusion matrix*).
4. **Sumber Data:** Dataset publik Yudi Wibisono (1.623 baris).

## Skenario dan Prosedur Pengujian
Eksperimen dilakukan dengan prosedur ketat:
1. **Pemuatan Data:** Konversi label (Normal=0, Spam=1).
2. **Pembersihan Teks:** *Case folding, tokenizing, stopword removal,* dan *stemming* (Sastrawi).
3. **Ekstraksi Fitur:** Transformasi teks menggunakan TF-IDF *Vectorizer*.
4. **Pelatihan:** Pembagian data 80:20 (*random_state=42*) pada Skenario A (*Naïve Bayes*) dan Skenario B (*SVM*).
5. **Validasi:** Penggunaan 10-*Fold Cross-Validation* untuk menjamin keadilan pengujian.

## Artifact dan Setup Implementasi
Penelitian menggunakan *Artefak Pipeline Komputasi* berupa skrip Python di Google Colab:
1. **Pandas & NumPy:** Manajemen tabel dan array matriks.
2. **Sastrawi Library:** Reduksi variasi morfologi bahasa Indonesia.
3. **Scikit-Learn:** *Engine* utama untuk TF-IDF, klasifikasi (SVM/NB), dan *GridSearchCV*.

## Teknik Analisis, Asumsi, dan Validitas
* **Teknik Analisis:** Perbandingan matematis langsung (*side-by-side*) antar metrik performa.
* **Asumsi:** Label dataset sekunder dianggap valid dan model spesifik untuk SMS pendek.

| Jenis Ancaman | Bentuk Ancaman | Mitigasi Risiko |
| :--- | :--- | :--- |
| **Internal Validity** | *Data Leakage* pada TF-IDF | `fit_transform` hanya pada data latih, `transform` pada data uji. |
| **Construct Validity** | Ketidakseimbangan kelas | Wajib menyertakan *Precision* dan *Recall*, tidak hanya akurasi. |
| **External Validity** | Generalisasi ke aplikasi lain | Penjelasan eksplisit mengenai keterbatasan korpus SMS di kesimpulan. |