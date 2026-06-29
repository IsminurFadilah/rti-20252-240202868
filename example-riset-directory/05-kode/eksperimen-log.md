# Catatan Eksperimen Model

Berikut adalah rekap performa perbandingan antara model *baseline* dan model intervensi.

## Log Pengujian (10-Fold Cross Validation)

| Tanggal | Model | Parameter | Akurasi | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| 25-06-2026 | Naive Bayes | default | 91.2% | Baseline awal |
| 25-06-2026 | SVM RBF | C=1.0, gamma='scale' | 96.5% | Hasil optimal setelah GridSearchCV |

## Analisis Kesalahan
* **Masalah:** Model SVM masih salah mengklasifikasikan pesan spam yang menggunakan singkatan gaul ekstrem.
* **Tindakan:** Perlu penambahan kamus *slang* (bahasa gaul) pada tahap `preprocessing.py`.