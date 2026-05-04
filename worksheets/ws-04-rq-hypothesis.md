# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Dataset yang terbatas serta penggunaan metode SVM tanpa perbandingan mendalam dengan metode lain menyebabkan belum diketahui metode yang paling optimal untuk klasifikasi SMS spam.

Research Question:
  Tipe         : [✔ ] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah metode Support Vector Machine menghasilkan performa yang lebih baik dibandingkan Naive Bayes dalam klasifikasi SMS spam berbahasa Indonesia berdasarkan metrik akurasi, precision, dan recall?
  Variabel IV  : Jenis algoritma (SVM vs Naive Bayes)
  Variabel DV  : Performa klasifikasi
  Metrik       : Akurasi, Precision, Recall
  Dataset      : Dataset SMS berbahasa Indonesia (±1623 data)
  Baseline     : Naive Bayes

Quality Check RQ:
  [✔ ] Variabel spesifik
  [✔ ] Metrik jelas
  [✔ ] Baseline ada
  [✔ ] Konteks disebutkan
  [✔ ] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Diketahui metode mana yang memiliki performa lebih baik dalam klasifikasi SMS spam berbahasa Indonesia berdasarkan evaluasi metrik yang terukur
  Jenis kontribusi        : [ ] Improvement  [ ] Comparison  [✔ ] Novel approach
  Gap yang diisi          : Method Gap (kurangnya perbandingan metode) + Data Gap

Hypothesis Pair:
  H₀ : Tidak terdapat perbedaan signifikan antara performa SVM dan Naive Bayes dalam klasifikasi SMS spam berdasarkan akurasi, precision, dan recall
  H₁ : Terdapat perbedaan signifikan antara performa SVM dan Naive Bayes dalam klasifikasi SMS spam berdasarkan akurasi, precision, dan recall
  Threshold              : 0.05 (significance level)
  Justifikasi threshold  : Nilai 0.05 merupakan standar umum dalam penelitian untuk menentukan signifikansi statistik
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Method Gap (belum ada perbandingan metode secara mendalam)

**RQ versi pertama (tulis bebas):**
> Metode mana yang lebih baik untuk klasifikasi SMS spam?

**Evaluasi RQ:**

| Komponen        | Ada? | Isi                        |
| --------------- | ---- | -------------------------- |
| Metode spesifik | ✔    | SVM vs Naive Bayes         |
| Metrik terukur  | ✔    | Akurasi, Precision, Recall |
| Baseline        | ✔    | Naive Bayes                |
| Dataset/konteks | ✔    | SMS Indonesia              |


**Tipe RQ:** [✔ ] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah metode Support Vector Machine menghasilkan performa yang lebih baik dibandingkan Naive Bayes dalam klasifikasi SMS spam berbahasa Indonesia berdasarkan metrik akurasi, precision, dan recall?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen              | Isi                                                       |
| --------------------- | --------------------------------------------------------- |
| H₀                    | Tidak ada perbedaan signifikan antara SVM dan Naive Bayes |
| H₁                    | Ada perbedaan signifikan antara SVM dan Naive Bayes       |
| Metrik                | Akurasi, Precision, Recall                                |
| Threshold             | 0.05                                                      |
| Justifikasi threshold | Standar umum penelitian                                   |


**Apakah hipotesis ini falsifiable?** [✔ ] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan melakukan eksperimen dan uji statistik (misalnya uji t), jika hasil menunjukkan perbedaan signifikan (p-value < 0.05), maka H₀ ditolak

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap           | Isi                                                               |
| --------------- | ----------------------------------------------------------------- |
| RQ              | Apakah SVM lebih baik dari Naive Bayes dalam klasifikasi SMS spam |
| Variable (IV)   | Jenis algoritma (SVM vs Naive Bayes)                              |
| Variable (DV)   | Performa klasifikasi                                              |
| Metric          | Akurasi, Precision, Recall                                        |
| Data source     | Dataset SMS Indonesia                                             |
| Analysis method | Perbandingan hasil + uji statistik                                |


**Apakah rantai lengkap?** [✔ ] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Deteksi SMS Spam Berbahasa Indonesia Menggunakan SVM
**RQ yang diekstrak:** Apakah metode SVM efektif dalam mendeteksi SMS spam berbahasa Indonesia?
**Komponen yang hilang:** 
- Tidak ada baseline pembanding
- Tidak menyebutkan metrik secara eksplisit