# Tahap 3 — Skrip Pengujian k6 (Legitimate vs Attack Traffic)

**Status:** Selesai — Matrix 10-Fold Cross-Validation selesai dijalankan, data tersedia di `/06-output/`
**Bergantung pada:** [tahap-2-implementasi-gateway.md](tahap-2-implementasi-gateway.md)
**Lokasi kode:** [../05-kode/k6](../05-kode/k6)

---

## Tujuan

Menyusun skrip eksekusi eksperimen untuk membandingkan model pada mode `Baseline` (Naïve Bayes) vs `Optimized` (SVM dengan Kernel RBF), dengan mengukur:

- **Performa Klasifikasi** — Akurasi, Precision, dan Recall pada data uji yang identik.
- **Efisiensi Komputasi** — Waktu eksekusi *training* dan *prediction* antar model.
- **Stabilitas Model** — Konsistensi hasil menggunakan 10-Fold Cross-Validation.

## Deliverable

- [x] Skrip `baseline_model.py` (implementasi Naïve Bayes) sesuai [ws-10-execution-data.md](../worksheets/ws-10-execution-data.md)
- [x] Skrip `optimized_model.py` (implementasi SVM + GridSearchCV)
- [x] Skrip `cross_validation.py` (pengaturan 10-fold sesuai [ws-07-experiment-design.md](../worksheets/ws-07-experiment-design.md))
- [x] Konfigurasi parameter (GridSearchCV space, random_state=42)
- [x] Output log eksperimen + Confusion Matrix (CSV/PNG) untuk Tahap 4
- [x] Smoke test (kalibrasi *preprocessing* & *vectorization*)

## Desain Eksperimen


### Struktur Kode (`05-kode/eksperimen/`)

```
05-kode/eksperimen/
├── data/
│   └── sms_spam.csv          # Dataset 1.623 baris
├── config.py                 # Parameter random_state, fold-size
├── baseline.py               # MultinomialNB
├── svm_optimized.py          # SVC + GridSearchCV
├── runner.py                 # Loop utama (10-Fold CV)
└── utils/
└── metrics.py            # Custom wrapper akurasi, precision, recall
```

## Matrix Eksperimen

| Dimensi | Nilai |
|---|---|
| **Model** | Naïve Bayes, SVM (RBF) |
| **Teknik Validasi** | 10-Fold Cross-Validation |
| **Split Ratio** | 80:20 (Training:Testing) |
| **Replikasi** | 10 Iterasi |

Total: **2 model × 10 iterasi = 20 hasil eksperimen**, dijalankan via `runner.py`.

## Hasil Eksperimen (Ringkasan)

Data disimpan dalam struktur `/06-output/<model>_<fold>_<timestamp>/`.
Setiap run mencakup:
1. `metrics.json` (akurasi, precision, recall, f1-score).
2. `confusion_matrix.png` (visualisasi *true positive* vs *false positive*).
3. `execution_time.log` (durasi *training* & *predict*).

## Catatan Lingkungan

- **Google Colab:** Digunakan sebagai *runner* utama untuk menyeimbangkan kebutuhan komputasi SVM pada *dataset* 1.623 baris.
- **Reproduksibilitas:** Penggunaan `random_state=42` pada `train_test_split` dan `GridSearchCV` memastikan hasil yang sama jika eksperimen dijalankan ulang.
- **Transien Error:** Jika terjadi *memory error* pada saat *GridSearchCV* melakukan iterasi *hyperparameter* yang terlalu banyak, disarankan untuk mempersempit *search space* pada `C` dan `gamma`.