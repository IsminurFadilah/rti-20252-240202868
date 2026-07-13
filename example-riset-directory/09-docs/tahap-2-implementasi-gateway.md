# Tahap 2 — Implementasi Pipeline Klasifikasi & Eksperimen

**Status:** Selesai
**Acuan Arsitektur:** [tahap-1-arsitektur-dan-skema-databa.md](tahap-1-arsitektur-dan-skema-databa.md)
**Lokasi Kode/Notebook:** [../05-kode/eksperimen/](../05-kode/eksperimen/)

---

## Tujuan

Mengimplementasikan *pipeline* klasifikasi teks menggunakan Python yang mendukung dua mode eksperimen untuk perbandingan kinerja:

- **Baseline (`None`):** Naïve Bayes (klasik) tanpa optimasi parameter.
- **Intervensi (`Hybrid/Optimized`):** SVM dengan *Kernel RBF* dan optimasi parameter via `GridSearchCV` untuk mencapai performa klasifikasi maksimal.

## Deliverable

- [x] **Struktur Project:** Notebook/Script Python dengan pemisahan *module* (`preprocessing.py`, `models.py`, `evaluation.py`).
- [x] **Data Ingestion:** Skrip *loader* dataset 1.623 SMS (format CSV/Pandas DataFrame).
- [x] **Preprocessing Pipeline:** Implementasi `Sastrawi` (stemming) dan `TfidfVectorizer` (TF-IDF).
- [x] **Model Baseline:** Implementasi `MultinomialNB` dari `scikit-learn`.
- [x] **Model Intervensi:** Implementasi `SVC` dengan optimasi `GridSearchCV` (C, gamma, kernel).
- [x] **Evaluasi:** Implementasi metrik `accuracy_score`, `precision_score`, `recall_score`, `f1_score`, dan `confusion_matrix`.
- [x] **Cross-Validation:** Implementasi `StratifiedKFold` (10-fold) untuk memastikan stabilitas hasil perbandingan.
- [x] **Logging:** Penyimpanan hasil eksperimen ke dalam format `.csv` di folder `06-output/`.

## Hasil Verifikasi Eksperimen

Diverifikasi melalui eksekusi *notebook* dengan hasil sebagai berikut:

- **Naïve Bayes:** Berhasil berjalan stabil dengan efisiensi waktu eksekusi yang sangat cepat (detik). Akurasi dasar tercatat di angka 0.93.
- **SVM (Optimized):** Berhasil melewati tahap *GridSearchCV* untuk menemukan parameter terbaik. Akurasi meningkat mencapai 0.94 dengan stabilitas *precision* yang lebih baik pada kelas spam.
- **Validitas:** Tidak ditemukan *error* pada *pipeline* saat melakukan *deployment* model ke data uji (20% data *hold-out*).
- **Integrasi:** Skrip evaluasi berhasil menghasilkan tabel perbandingan performa yang konsisten.

## Catatan Lingkungan

- **Python Version:** 3.9+ dengan `scikit-learn` terbaru.
- **Environment:** Google Colab digunakan untuk memanfaatkan kemudahan *library* `Sastrawi`.
- **Dependency:** Pastikan `pip install sastrawi scikit-learn pandas` sudah dijalankan di lingkungan *local* jika ingin melakukan *reproducibility* offline.
- **Data Path:** Pastikan file dataset (`spam.csv`) terletak di path yang benar sesuai `config.yaml` agar tidak terjadi *file-not-found error* saat *runtime*.