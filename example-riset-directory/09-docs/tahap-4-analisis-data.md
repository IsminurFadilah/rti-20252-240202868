# Tahap 4 — Analisis Data & Visualisasi Performa Model

**Status:** Selesai — pipeline analisis telah dijalankan pada 10-fold CV matrix, statistik dan visualisasi tersedia di `/06-output/`
**Bergantung pada:** [tahap-3-pengujian-eksperimen.md](tahap-3-pengujian-eksperimen.md)
**Lokasi kode:** [../05-kode/analysis/](../05-kode/analysis/)

---

## Tujuan

Mengolah hasil eksperimen mentah dari 10-fold Cross-Validation (Naïve Bayes vs SVM) untuk menghasilkan statistik deskriptif, pengujian hipotesis statistik (T-Test), dan visualisasi performa model guna keperluan penulisan jurnal pada Tahap 5.

## Deliverable

- [x] Skrip agregasi metrik dari `/06-output/` (`aggregate_results.py`)
- [x] Perhitungan statistik deskriptif (Mean & Std Dev) untuk Akurasi, Precision, Recall, F1-Score
- [x] Pengujian Signifikansi Statistik (Paired T-Test) untuk memvalidasi perbedaan performa model
- [x] Visualisasi: Grafik Bar Perbandingan Performa & Heatmap Confusion Matrix
- [x] Tabel Ringkasan Eksperimen untuk Naskah Jurnal (`/06-output/tables/summary.md`)
- [x] Orkestrator `run_analysis.py` untuk generate seluruh laporan statistik

## Desain Analisis

### Struktur kode (`05-kode/analysis/`)

```
05-kode/analysis/
├── requirements.txt       # pandas, scipy, matplotlib, seaborn
├── load_data.py           # Reader untuk file CSV hasil eksperimen
├── stats_test.py          # Paired T-Test (scipy.stats)
├── confusion_matrix.py    # Generate heatmap dari raw matrix
├── charts.py              # Bar plot (Akurasi/F1) & Boxplot
└── run_analysis.py        # Eksekusi seluruh pipeline analisis
```

## Definisi Metrik

Analisis dilakukan berdasarkan:
- **Akurasi:** Rasio prediksi benar terhadap total data.
- **F1-Score:** Harmonic mean dari Precision & Recall (penting karena fokus pada deteksi *spam*).
- **Paired T-Test:** Membandingkan nilai akurasi pada *fold* yang sama untuk kedua model ($p < 0.05$ dianggap signifikan).

## Hasil Analisis

### 1. Statistik Deskriptif (Mean ± Std)

| Model | Akurasi | F1-Score | Std Dev (Acc) |
| :--- | :--- | :--- | :--- |
| **Naïve Bayes** | 0.931 | 0.925 | 0.021 |
| **SVM (RBF)** | 0.942 | 0.938 | 0.012 |

### 2. Signifikansi Statistik
Hasil uji *Paired T-Test* menunjukkan nilai $p = 0.065$. Karena $p > 0.05$, secara statistik perbedaan performa antara SVM dan Naïve Bayes **tidak signifikan secara absolut**, meskipun SVM menunjukkan stabilitas (*standard deviation*) yang lebih rendah.



### 3. Temuan Kunci
- **Stabilitas:** SVM memiliki standar deviasi yang lebih kecil (0.012 vs 0.021), menunjukkan bahwa SVM lebih stabil terhadap variasi data *fold* dibandingkan Naïve Bayes.
- **Efektivitas:** Meskipun SVM unggul di rata-rata akurasi, peningkatan tersebut tidak drastis, sehingga Naïve Bayes tetap menjadi kandidat kuat jika efisiensi waktu komputasi menjadi prioritas.
- **Bottleneck:** Kasus *False Negative* pada Naïve Bayes lebih tinggi, yang berarti ada beberapa pesan *spam* yang terdeteksi sebagai *ham* (normal).

---

## Catatan untuk Tahap 5
- Temuan mengenai **"Performa Kompetitif"** dan **"Stabilitas SVM"** akan menjadi narasi utama dalam bagian *Discussion* di draf jurnal.
- Visualisasi (Bar Chart & Confusion Matrix) akan disisipkan ke dalam draf manuskrip sebagai Figure 1 dan Figure 2.