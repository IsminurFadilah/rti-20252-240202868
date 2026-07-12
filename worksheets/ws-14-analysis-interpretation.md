# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

## 1. Statistik Deskriptif:
| Skenario | Mean | Std | Median | Min | Max | n |
|----------|------|-----|--------|-----|-----|---|
| SVM      | 0.94 | 0.01| 0.94   | 0.93| 0.95| 10|
| Naive Bayes| 0.93 | 0.02| 0.93   | 0.91| 0.95| 10|

## 2. Uji Hipotesis:
   Uji yang digunakan   : Paired T-Test (Asumsi: n=10 per model)
   Justifikasi          : Membandingkan performa dua model pada dataset yang sama (paired samples).
   Hasil: p = 0.065, effect size (d) = 0.62
   CI 95%               : [-0.001, 0.021]

## 3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [x] H₀ tidak ditolak (karena p > 0.05)

## 4. Interpretasi:
   Hubungan ke RQ        : Tidak ada perbedaan signifikan secara statistik antara SVM dan NB dalam deteksi SMS spam pada ukuran dataset ini.
   Practical significance: Perbedaan 1% mungkin berarti bagi akurasi model, namun tidak signifikan secara statistik.
   Perbandingan literatur: Sejalan dengan penelitian NLP pada dataset kecil dimana algoritma sederhana (NB) mampu bersaing dengan SVM.

## 5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Data  | Ukuran kecil | Generalisasi terbatas | Tambah volume dataset |
   | Stat  | N rendah (10) | Power test rendah | Tambah iterasi/k-fold CV |

## 6. Failure Analysis:
   Penyebab potensial  : Ukuran dataset 500 baris terlalu kecil untuk melihat perbedaan *hyperplane* SVM secara signifikan dibandingkan probabilitas NB.
   Boundary condition   : Kinerja setara pada data bersih, kemungkinan berbeda pada data yang lebih *noisy*.
   Insight              : Pada dataset skala kecil, pemilihan model tidak bersifat kritis; *feature engineering* lebih berpengaruh.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 (SVM dan Naive Bayes) |
| Apakah data berpasangan (paired)? | Ya |
| Apakah distribusi normal? | Ya (asumsi CLT untuk n=10) |
| **Uji yang dipilih:** | Paired T-Test |
| **Justifikasi:** | Perbandingan performa dua model pada data uji yang sama. |

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 89.2 ± 1.5 | 10 |
| B | 87.8 ± 2.1 | 10 |

p = 0.045, Cohen's d = 0.74, CI 95% = [0.03, 2.77]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p=0.065, tidak signifikan pada level alpha 0.05. |
| Effect size | d=0.62 (medium effect), menunjukkan SVM memiliki kecenderungan lebih baik. |
| Practical significance | Perbedaan performa belum memberikan keuntungan operasional yang drastis. |
| Hubungan ke RQ | SVM performanya stabil, namun NB lebih efisien secara komputasi. |
| Perbandingan literatur | NB tetap menjadi baseline yang sulit dikalahkan oleh SVM pada dataset teks kecil. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Tidak, ini adalah hasil "null" yang valid dalam riset. |
| Kemungkinan penyebab? | Overfitting ringan pada SVM atau underfitting pada NB karena dataset kurang variatif. |
| Boundary condition? | SVM mungkin unggul jika data diperbesar hingga 5.000+ baris. |
| Insight yang bisa diambil? | Tidak perlu kompleksitas model jika performa baseline sudah mencapai >90%. |
| Apakah layak dilaporkan? | Sangat layak untuk memberikan perspektif objektif bagi pembaca. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical | Ukuran sampel (N=10) | Hasil tidak cukup kuat untuk menolak H₀ |


---

## Refleksi

> **Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?**

> Failure analysis adalah kontribusi penting karena memberikan transparansi. Hasil negatif mengajarkan bahwa tidak semua masalah klasifikasi teks membutuhkan algoritma berat seperti SVM, sehingga peneliti berikutnya bisa memilih pendekatan yang lebih efisien (seperti Naive Bayes).

> **Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?**
> Saya melihatnya bukan sebagai kekalahan model, melainkan sebagai "batasan" (boundary) di mana model tersebut bekerja optimal. Ini membuat riset saya lebih kredibel karena tidak melakukan klaim berlebihan terhadap model yang saya buat.
