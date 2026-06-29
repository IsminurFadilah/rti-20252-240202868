# 05-kode

Implementasi skrip pemrograman Python untuk tahapan riset klasifikasi teks SMS Spam.

## Struktur Direktori

- `notebook/` : Berisi *Jupyter Notebook* untuk prototyping eksperimen dan visualisasi data awal.
- `src/` : Kumpulan modul Python untuk *pipeline* klasifikasi.
- `requirements.txt` : Daftar dependensi pustaka yang digunakan (Sastrawi, Scikit-Learn, Pandas).

## Modul Utama

1. **`preprocessing.py`** : Skrip khusus untuk *Case Folding*, *Tokenizing*, *Stopword Removal*, dan *Stemming* menggunakan pustaka `Sastrawi`.
2. **`model_nb.py`** : Implementasi algoritma *Baseline* Naive Bayes untuk klasifikasi SMS.
3. **`model_svm.py`** : Implementasi algoritma utama SVM dengan optimasi `GridSearchCV` untuk mencari parameter terbaik (C, gamma, kernel).
4. **`utils.py`** : Fungsi utilitas untuk memuat dataset dari `../04-data/` dan fungsi generik untuk menghitung *Confusion Matrix*.

## Catatan Eksekusi
Pastikan lingkungan virtual Python telah terinstal sebelum menjalankan skrip:
```bash
pip install -r requirements.txt
python src/model_svm.py