# 06-output

Hasil olahan data, visualisasi performa model, dan log eksperimen — **Tahap 5** (Analisis Performa Model).

Dihasilkan oleh skrip eksekusi di `05-kode/src/` berdasarkan dataset dari `04-data/`.

##  Tabel Hasil Eksperimen (`tables/`)

| File | Isi |
| :--- | :--- |
| `performa_model.csv` | Ringkasan metrik akurasi, presisi, recall, dan F1-score untuk Naive Bayes & SVM. |
| `hasil_cross_validation.csv` | Log detail akurasi dari 10-fold cross-validation untuk tiap model. |
| `error_analysis.csv` | Daftar sampel SMS yang salah diprediksi oleh model (False Positives/Negatives). |

##  Visualisasi Data (`figures/`)

| File | Isi |
| :--- | :--- |
| `fig_akurasi_comparison.png` | Bar chart perbandingan akurasi rata-rata antara Naive Bayes dan SVM. |
| `fig_cm_naive_bayes.png` | *Confusion Matrix* (Heatmap) untuk model Naive Bayes. |
| `fig_cm_svm.png` | *Confusion Matrix* (Heatmap) untuk model SVM dengan kernel RBF. |
| `fig_learning_curve.png` | Kurva pembelajaran untuk melihat potensi *overfitting* pada model SVM. |

##  Catatan Tambahan

- Data di folder ini digunakan sebagai dasar argumentasi dalam bab pembahasan di dokumen akhir.
