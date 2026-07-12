# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

**Research Question**: Manakah algoritma yang lebih efektif dalam mengklasifikasikan SMS spam: Support Vector Machine (SVM) atau Naive Bayes?  
**Metrik Utama**: Akurasi (Accuracy)

### Tabel Hasil:
| Skenario | Akurasi (mean ± std) | F1-Score (mean ± std) | n |
|----------|----------------------|----------------------|---|
| SVM      | 0.94 ± 0.01          | 0.93 ± 0.02          | 10 |
| Naive Bayes | 0.93 ± 0.02       | 0.92 ± 0.02          | 10 |

### Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|--------------|-------------|--------|
| 1 | Bar chart + error bar | Perbandingan akurasi SVM vs Naive Bayes | Mean Accuracy ± Std |
| 2 | Box plot | Perbandingan variabilitas performa F1-Score | Distribusi F1-Score |

### Bias Check:
- [x] Y-axis mulai dari 0 (atau dijustifikasi)
- [x] Error bar/CI ditampilkan
- [x] Semua data disertakan (tidak cherry-picked)
- [x] Tidak menggunakan 3D tanpa alasan

---

## Latihan 1 — Tabel Hasil

| Skenario | Akurasi (mean ± std) | F1-Score (mean ± std) | n |
|----------|----------------------|----------------------|---|
| SVM      | 0.94 ± 0.01 | 0.93 ± 0.02 | 10 |
| Naive Bayes | 0.93 ± 0.02 | 0.92 ± 0.02 | 10 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|--------------|-------|---------------------|
| 1 | Bar chart + error bar | SVM memiliki akurasi sedikit lebih tinggi dan stabil dibandingkan Naive Bayes. | Mean accuracy ± std |
| 2 | Box plot | Rentang performa F1-Score SVM lebih konsisten (sempit) daripada Naive Bayes. | Semua run F1-Score |

---

## Latihan 3 — Bias Detection

**Evaluasi skenario (Metode A 91.2% vs Metode B 90.8%, Y-axis mulai dari 90%):**

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya, karena perbedaan 0.4% terlihat sangat signifikan secara visual padahal tipis. |
| Apakah error bar ditampilkan? | Tidak disebutkan dalam skenario. |
| Apakah semua kondisi ditampilkan? | Ya, hanya dua kondisi. |
| Apa solusinya? | Memulai Y-axis dari 0 agar perbedaan proporsional dan jujur. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: N/A

---

## Refleksi

> **Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja?**
> Tabel diperlukan untuk memberikan data yang presisi dan akurat bagi pembaca yang ingin meninjau angka spesifik (tanggung jawab ilmiah). Grafik diperlukan untuk memberikan pemahaman pola dan perbandingan yang cepat bagi pembaca, karena otak manusia lebih mudah mencerna informasi visual daripada deretan angka.

> **Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?**
> Pernah, terutama saat mencoba memotong sumbu Y untuk membuat perbedaan antar data terlihat lebih "dramatis" di presentasi agar terlihat lebih unggul. Saya menyadari sekarang bahwa dalam konteks riset, kejujuran data (transparansi sumbu) jauh lebih penting daripada estetika visual yang manipulatif.
