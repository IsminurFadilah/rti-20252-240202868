# Tahap 1 — Perancangan Pipeline Klasifikasi & Skema Data

**Status:** Selesai

---

## 1. Komponen Sistem

1. **Environment Python (Google Colab / Jupyter)** — sebagai *engine* utama untuk eksekusi eksperimen, manajemen data, dan pemrosesan komputasi model.
2. **Preprocessing Pipeline (Sastrawi)** — melakukan pembersihan teks otomatis untuk menstandarisasi bahasa Indonesia (menangani variasi imbuhan dan kata tidak baku).
3. **Model Klasifikasi (Scikit-Learn)** — menggunakan arsitektur *Supervised Learning* untuk pemodelan:
   - **Baseline:** Algoritma Naïve Bayes.
   - **Intervensi:** Algoritma Support Vector Machine (SVM) dengan *Kernel RBF*.
4. **Data (Dataset Yudi Wibisono)** — 1.623 baris SMS terlabeli sebagai *Source of Truth* eksperimen.

## 2. Alur Kerja (Pipeline Eksperimen)
Dataset (1.623 SMS)
│
├─ Preprocessing (Case Folding → Tokenizing → Stopword Removal → Stemming)
│
├─ Ekstraksi Fitur (TF-IDF Vectorizer)
│
├─ Pembagian Data (Train 80% / Test 20%, random_state=42)
│
├─ Skenario A (Baseline: Naïve Bayes)
│     └─ Pelatihan → Prediksi → Evaluasi (Akurasi, Precision, Recall)
│
└─ Skenario B (Intervensi: SVM + GridSearchCV)
└─ Optimasi Parameter → Pelatihan → Prediksi → Evaluasi (Akurasi, Precision, Recall)

**Catatan:** Kedua skenario dijalankan pada lingkungan yang identik (*fairness*) dengan validasi silang (10-Fold Cross-Validation) untuk memastikan objektivitas perbandingan antara performa Naïve Bayes dan SVM.

## 3. Struktur Data (Format Dataset)

Dataset menggunakan label biner untuk klasifikasi:

```csv
id,text,label
1,"Info promo menarik dari operator X...","spam"
2,"Halo, ibu sudah sampai rumah?","ham"
...

**Transformasi Internal (Encoding):**
- **Label 0:** `ham` (normal)
- **Label 1:** `spam` (gangguan/penipuan)
```

## 4. Konfigurasi Eksperimen

| Komponen | Spesifikasi | Tujuan |
| :--- | :--- | :--- |
| **Library** | Scikit-Learn (0.24+) | Engine matematika dan ML |
| **Stemmer** | Sastrawi | Reduksi morfologi kata Indonesia |
| **Vectorizer** | TF-IDF | Representasi matriks teks |
| **Optimasi** | GridSearchCV | Penalaan parameter otomatis pada SVM |

## 5. Keputusan Teknis (Final)

1. **Fairness:** Semua data uji (20%) disimpan secara terpisah dan identik untuk kedua model agar perbandingan apple-to-apple.
2. **Preprocessing:** Menggunakan Sastrawi secara konsisten pada semua fold validasi untuk menjaga validitas linguistik.
3. **Analisis:** Menggunakan classification_report dan confusion_matrix dari Scikit-Learn untuk membedah False Positive dan False Negative.
4. **Reproduksibilitas:** Seluruh alur (dari preprocessing hingga GridSearchCV) disimpan dalam skrip Python (.ipynb) yang dapat dijalankan ulang (reproducible).