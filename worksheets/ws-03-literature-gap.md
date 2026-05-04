# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Klasifikasi SMS spam berbahasa Indonesia
Database   : Google Scholar
Query      : "SMS spam Indonesia SVM TF-IDF Naive Bayes LSTM"
Tahun      : 2019 - 2024
Hasil awal : 15 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|Widyawati & Susanto|2019|Naive Bayes vs SVM|SMS Indonesia|Akurasi ±97%|Perbandingan Terbatas|
|Muslikah|2021|LSTM|SMS Indonesia|96.09%|Butuh resource tinggi|
|Dwiyansaputra et al.|2021|TF-IDF + SGD|SMS|±97%|Model sederhana|
|Theodorus et al.|2021|RF, SVM, XGBoost|SMS|SVM 94.38%|Belum optimal|
|Sofyan et al.|2024|SVM + TF-IDF|1623 SMS|96.94%|Dataset kecil|


Pola yang ditemukan:
  Metode dominan     : Machine Learning (SVM, Naive Bayes, TF-IDF)
  Dataset umum       : Dataset SMS berbahasa Indonesia
  Limitasi berulang  : - Dataset relatif kecil
                       - Fokus hanya klasifikasi biner
                       - Belum banyak eksplorasi metode modern

GAP IDENTIFICATION

Gap 1: [Jenis:  data gap]
  Deskripsi    : Dataset yang digunakan dalam penelitian masih terbatas jumlahnya sehingga belum mewakili kondisi nyata secara luas
  Bukti        : Jumlah dataset 1623 SMS
  Signifikansi : Dataset yang kecil dapat menyebabkan model kurang mampu melakukan generalisasi pada data baru dan berpotensi overfitting

Gap 2: [Jenis: method gap]
  Deskripsi    : Penelitian hanya menggunakan metode SVM tanpa melakukan perbandingan mendalam dengan metode lain
  Bukti        : Model utama yang digunakan adalah SVM dengan TF-IDF
  Signifikansi : Belum diketahui apakah SVM merupakan metode terbaik dibandingkan metode lain seperti LSTM atau Naive Bayes

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|Naive Bayes|Sama-sama klasifikasi SMS|Banyak digunakan|Widyawati, 2019|
|LSTM|Alternatif deep learning|Digunakan di penelitian lain|Muslikah, 2021|
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Klasifikasi SMS spam berbahasa Indonesia
**Query pencarian:** "SMS spam Indonesia SVM LSTM TF-IDF"
**Database:** Google Scholar

| # | Study           | Tahun | Method       | Dataset | Result | Limitasi        |
| - | --------------- | ----- | ------------ | ------- | ------ | --------------- |
| 1 | Widyawati       | 2019  | NB vs SVM    | SMS     | 97%    | Terbatas        |
| 2 | Muslikah        | 2021  | LSTM         | SMS     | 96%    | Resource tinggi |
| 3 | Dwiyansaputra   | 2021  | TF-IDF + SGD | SMS     | 97%    | Sederhana       |
| 4 | Theodorus       | 2021  | ML           | SMS     | 94%    | Kurang optimal  |
| 5 | Penelitian 2024 | 2024  | SVM          | SMS     | 96.94% | Data kecil      |


**Pola yang terlihat — Metode dominan:** SVM dan Machine Learning
**Limitasi yang berulang:** Dataset kecil

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap       | Ditemukan?         | Gap Statement                                                                     |
| --------------- | ------------------ | --------------------------------------------------------------------------------- |
| Performance Gap | [✔ ] Ya / [ ] Tidak | Model belum diuji pada kondisi real-world sehingga performa nyata belum diketahui |
| Method Gap      | [✔ ] Ya / [ ] Tidak | Metode SVM digunakan tanpa perbandingan mendalam dengan metode lain               |
| Data Gap        | [✔ ] Ya / [ ] Tidak | Dataset yang digunakan relatif kecil (1623 data) sehingga kurang representatif    |
| Context Gap     | [✔ ] Ya / [ ] Tidak | Penelitian hanya berfokus pada SMS dan belum diterapkan pada platform lain        |


**Gap utama yang dipilih:** Data Gap dan Method Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena dataset yang kecil membatasi kemampuan model dalam memahami variasi data, sementara penggunaan metode yang belum dibandingkan secara mendalam membuat performa model belum dapat dipastikan optimal.


---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline             | Mengapa Relevan                        | Mengapa Representatif                      | Apakah SOTA?                | Sumber                    |
| - | -------------------- | -------------------------------------- | ------------------------------------------ | --------------------------- | ------------------------- |
| 1 | Naive Bayes + TF-IDF | Task sama: klasifikasi SMS spam        | Banyak digunakan dalam penelitian SMS spam | Tidak, tapi common practice | Widyawati & Susanto, 2019 |
| 2 | LSTM                 | Digunakan untuk klasifikasi teks (NLP) | Mewakili pendekatan deep learning          | Hampir SOTA                 | Muslikah, 2021            |


**Apakah pemilihan baseline ini bisa dianggap straw man?** [✔ ] Ya / [ ] Tidak
> Justifikasi: Baseline yang dipilih merupakan metode yang umum digunakan dalam penelitian sebelumnya dan relevan dengan permasalahan yang sama, yaitu klasifikasi SMS spam. Naive Bayes mewakili pendekatan machine learning klasik yang sering digunakan, sedangkan LSTM mewakili pendekatan deep learning yang lebih modern. Dengan demikian, perbandingan dilakukan secara adil dan tidak menggunakan metode yang lemah untuk membuat hasil penelitian terlihat lebih baik.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaan antara klaim “belum ada yang meneliti ini” dengan research gap yang valid terletak pada adanya bukti yang mendukung. Klaim tanpa bukti hanya berdasarkan asumsi pribadi, sedangkan research gap yang valid harus didasarkan pada hasil literature review yang sistematis, yang menunjukkan pola, keterbatasan, atau kekurangan dari penelitian sebelumnya.

> Cara membuktikan bahwa sebuah gap benar-benar ada adalah dengan melakukan pencarian literatur menggunakan database yang jelas dan query yang terstruktur, kemudian melakukan screening terhadap paper yang relevan. Selanjutnya, dilakukan analisis untuk menemukan metode yang dominan, keterbatasan yang berulang, serta bagian yang belum optimal atau belum dieksplorasi. Dengan demikian, gap yang diidentifikasi memiliki dasar yang kuat dan dapat dipertanggungjawabkan secara ilmiah.
