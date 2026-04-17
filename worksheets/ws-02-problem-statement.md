# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Text Mining 
  Konteks  : Deteksi SMS spam berbahasa Indonesia pada perangkat komunikasi

System Context
  Input       : Teks SMS dari pengguna
  Process     : Preprocessing teks dan klasifikasi menggunakan metode SVM
  Output      : Label klasifikasi (spam / non-spam)
  Outcome     : Membantu pengguna mengidentifikasi SMS spam secara otomatis
  Constraints : Dataset terbatas, variasi bahasa tidak selalu sama, model tidak 100% akurat
  Stakeholders: Pengguna ponsel, peneliti, pengembang sistem

Fenomena → Problem
  Fenomena yang diamati             : Banyaknya SMS spam yang diterima pengguna
  Gejala (symptom) yang terukur     : Pesan promosi atau penipuan sering muncul dan mengganggu
  Masalah yang didiagnosis          : Tidak adanya sistem otomatis untuk membedakan SMS spam dan non-spam
  Masalah riset (researchable)      : Bagaimana mengklasifikasikan SMS spam berbahasa Indonesia menggunakan metode SVM dengan akurasi yang baik
  Variabel yang terukur             : Akurasi, precision, recall dari hasil klasifikasi

Problem Quality Check
  [✓] Clarity
  [✓] Measurability
  [✓] Relevance
  [✓] Testability
  [✓] Impact

Problem Statement (1 paragraf):
  Banyaknya SMS spam yang diterima oleh pengguna ponsel menyebabkan gangguan dan potensi penipuan. Namun, belum terdapat sistem yang mampu secara otomatis mengklasifikasikan SMS berbahasa Indonesia menjadi spam dan non-spam dengan akurat. Oleh karena itu, penelitian ini bertujuan untuk mengkaji penggunaan metode Support Vector Machine dalam mengklasifikasikan SMS spam dengan mengukur performa menggunakan metrik seperti akurasi, precision, dan recall.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Deteksi SMS spam berbahasa Indonesia

| Tahap | Hasil |
|-------|-------|
| Reality | Banyak pengguna menerima SMS spam |
| Observed Issue (Symptom) | Banyak SMS promosi dan penipuan yang mengganggu |
| Diagnosed Problem (Root Cause) | Tidak ada sistem otomatis untuk memfilter SMS spam |
| Researchable Problem | Bagaimana mengklasifikasikan SMS spam menggunakan metode SVM |
| Measurable Variable | Akurasi, precision, recall |

**Apakah terjebak solution-first thinking?** [ ] Ya / [✓] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Teks SMS dari pengguna |
| Process | Preprocessing teks dan klasifikasi menggunakan SVM |
| Output | Label spam atau non-spam |
| Outcome | Pengguna dapat mengetahui SMS spam secara otomatis |
| Constraints | Dataset terbatas dan variasi bahasa |
| Stakeholders | Pengguna, peneliti, pengembang |

**Komponen mana yang paling relevan dengan masalah riset?** Process

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Masalah dijelaskan dengan jelas |
| Measurability | 5 | Menggunakan metrik akurasi, precision, recall |
| Relevance | 5 | Masalah spam sangat umum terjadi |
| Testability | 5 | Bisa diuji dengan eksperimen |
| Impact | 4 | Memberikan solusi bagi pengguna |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
>Banyaknya SMS spam yang diterima pengguna menjadi masalah yang mengganggu dan berpotensi menimbulkan kerugian. Saat ini belum terdapat sistem otomatis yang efektif dalam mengklasifikasikan SMS berbahasa Indonesia menjadi spam dan non-spam. Oleh karena itu, penelitian ini bertujuan untuk menganalisis penggunaan metode Support Vector Machine dalam mendeteksi SMS spam dengan mengukur performa menggunakan metrik akurasi, precision, dan recall.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah dalam coding umumnya bersifat teknis dan langsung terlihat, seperti error, bug, atau fitur yang tidak berjalan sesuai harapan, sehingga pendekatannya adalah mencari penyebab langsung lalu memperbaikinya agar sistem dapat berfungsi dengan baik. Sebaliknya, dalam riset, masalah tidak selalu terlihat secara langsung dan lebih berupa fenomena yang perlu dianalisis secara mendalam, seperti pada kasus SMS spam yang tidak hanya dilihat sebagai gangguan, tetapi diteliti bagaimana metode tertentu mampu mendeteksinya secara akurat. Pendekatan dalam riset bersifat sistematis dan terstruktur, dimulai dari identifikasi gejala, penelusuran akar masalah, hingga perumusan masalah yang dapat diuji secara ilmiah menggunakan data dan metode tertentu. Perbedaan fundamentalnya terletak pada tujuan dan cara berpikir, di mana coding berfokus pada penyelesaian masalah agar sistem berjalan (problem solving), sedangkan riset berfokus pada pemahaman dan pembuktian suatu fenomena melalui pengukuran yang jelas, seperti akurasi, serta melalui eksperimen yang dapat divalidasi.
