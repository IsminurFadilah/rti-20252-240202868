# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

**Slide Deck Plan:**
  Total slides   : 12 (Target: 15 menit)
  Time per slide : ~1.25 menit
  Total time     : 15 menit

**Anticipatory Defense Matrix (CER - Claim, Evidence, Reasoning):**
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa deteksi spam penting? | Spam mengancam privasi & efisiensi komunikasi. Data menunjukkan lonjakan volume pesan berbahaya. |
| Method   | Kenapa pilih SVM & NB? | Algoritma ini terbukti efisien untuk data teks biner. NB sebagai baseline, SVM untuk optimasi hyperplane. |
| Results  | Mengapa hasil tidak signifikan? | Dataset 500 baris memiliki variansi tinggi. Hasil menunjukkan model bersifat ekuivalen pada data skala kecil. |
| Generalization | Apakah bisa dipakai untuk bahasa lain? | Bergantung pada preprocessing. Model memerlukan adaptasi *stopword* dan *stemmer* bahasa lokal. |
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

## Latihan 1 — Slide Outline

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul, Penulis, & Agenda | Cover slide | 0.5 min |
| 2 | Problem: Ancaman Spam | Grafik statistik spam | 1.5 min |
| 3 | Gap + RQ | Tabel gap literatur | 1.5 min |
| 4 | Metodologi: Pipeline | Flowchart NLP | 2 min |
| 5 | Eksperimen: Setup | Tabel skenario model | 1.5 min |
| 6 | Hasil: Accuracy (Tabel) | Tabel perbandingan | 1.5 min |
| 7 | Hasil: Visualisasi | Bar chart + error bar | 1.5 min |
| 8 | Analisis: Statistik (T-test) | p-value & Cohen's d | 1.5 min |
| 9 | Diskusi: Interpretasi | Bullet points kunci | 1.5 min |
| 10 | Limitasi & Failure Analysis | Matriks batasan riset | 1 min |
| 11 | Kesimpulan & Masa Depan | Ringkasan temuan | 0.5 min |
| 12 | Q&A | Slide Penutup | - |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Pertanyaan | Claim | Evidence | Reasoning |
|---|-----------|-------|----------|-----------|
| 1 | Mengapa dataset cuma 500? | Data 500 mencukupi untuk baseline awal | Eksperimen berjalan stabil | Fokus pada validasi pipeline |
| 2 | Kenapa tidak pakai DL? | DL butuh resource besar | Hasil SVM > 90% | Overhead DL tidak sebanding manfaat |
| 3 | Bagaimana jika data tidak seimbang? | Dataset sudah di-split stratifikasi | Stratified split ratio | Memastikan label spam/ham terwakili |
| 4 | Apa kontribusi riset ini? | Penentuan boundary model | Hasil negatif yang valid | Mencegah riset duplikasi |
| 5 | Apa riset lanjutan? | Optimasi hyperparameter | Grid search scope | Perlu optimasi lebih lanjut |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | "Kenapa hasil tidak signifikan?" | "Dataset 500 belum cukup untuk memisahkan performa secara statistik." | [x] Direct [x] Data-based [x] Honest |
| 2 | "Apakah SVM ini optimal?" | "Belum, perlu dilakukan tuning hyperparameter C dan kernel lebih lanjut." | [x] Direct [x] Data-based [x] Honest |
| 3 | "Apa kelebihan NB dibanding SVM?" | "Kecepatan komputasi yang jauh lebih tinggi." | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> "Jika SVM dan Naive Bayes memberikan hasil yang hampir sama (tidak signifikan secara statistik), mengapa pembaca/industri harus memilih salah satu di antaranya?"

**Apa yang perlu disiapkan lebih baik:**
> 1. Menyiapkan tabel perbandingan **kompleksitas komputasi** (training time & inference time) secara eksplisit.
> 2. Menyiapkan skenario **kasus penggunaan** (contoh: untuk *real-time streaming* di perangkat low-end, NB jauh lebih unggul; untuk *batch processing* dengan akurasi maksimal, SVM lebih layak).
> 3. Mempertajam argumen tentang **stabilitas model** (bagaimana performa model saat diberikan data dengan noise/variasi baru).

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Bahwa riset yang "gagal" atau tidak signifikan secara statistik adalah bagian dari ilmu pengetahuan yang jujur. Fokus utama bukan memenangkan algoritma, melainkan memahami batasan (boundary condition) dari tiap metode.

**Yang akan selalu diterapkan:**
> Selalu melakukan `Consistency Matrix` sebelum menulis paper. Hal ini memastikan alur dari Introduction hingga Conclusion benar-benar saling mengunci, sehingga penguji tidak akan menemukan celah logika.
