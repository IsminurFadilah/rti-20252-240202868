# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [X] Problem → Gap: masalah terdokumentasi di literatur
      * Bukti: Masalah tingginya kasus SMS spam di Indonesia didukung oleh data Truecaller Insights Report 2020. Gap yang diangkat adalah perlunya optimasi model SVM (GridSearch & Cross-Validation) sekaligus implementasi praktisnya ke dalam sistem aplikasi web (Streamlit).
  [X] Gap → RQ: pertanyaan menjawab gap spesifik
      * Bukti: RQ secara spesifik mempertanyakan tingkat akurasi algoritma SVM setelah dioptimasi dengan GridSearch, serta bagaimana cara mengimplementasikannya ke dalam platform aplikasi Streamlit.
  [X] RQ → Hypothesis: hipotesis memprediksi jawaban
      * Bukti: Hipotesis memprediksi bahwa penerapan SVM dengan kernel RBF dan optimasi GridSearch mampu menghasilkan akurasi tinggi (mencapai >= 95%) dan sistem aplikasi web dapat berfungsi dengan baik.
  [X] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
      * Bukti: Variabel akurasi dalam hipotesis diukur menggunakan metrik standard klasifikasi teks, yaitu Accuracy, Precision, Recall, dan F1-Score yang dihitung dari Confusion Matrix.
  [X] Metric → System: komponen sistem menghasilkan/mengukur metrik
      * Bukti: Komponen tahap 'Evaluation' dalam arsitektur sistem CRISP-DM bertugas memproses data uji untuk menghitung dan mengeluarkan nilai metrik klasifikasi tersebut secara otomatis.
  [X] System → Experiment: desain eksperimen menggunakan sistem
      * Bukti: Desain eksperimen menguji pipeline sistem dengan membagi dataset (80% latih, 20% uji) dan menjalankan pengujian silang 10-fold Cross-Validation untuk mencari parameter SVM terbaik.

Koneksi Horizontal (Konsistensi):
  [X] Istilah sama di semua bagian
      * Bukti: Istilah kunci seperti "SMS Spam", "Support Vector Machine (SVM)", "TF-IDF", dan "Streamlit" digunakan secara konsisten dari latar belakang hingga bab evaluasi.
  [X] Variabel di RQ = variabel di hipotesis = metrik di desain
      * Bukti: Variabel bebas (parameter C, Gamma, TF-IDF) dan variabel terikat (metrik akurasi hasil klasifikasi) sama-sama konsisten ada di RQ, hipotesis, maupun metodologi eksperimen.
  [X] Scope tidak berubah dari masalah ke eksperimen
      * Bukti: Batasan masalah tetap konsisten fokus pada deteksi pesan teks SMS spam berbahasa Indonesia menggunakan metode supervised learning (SVM).

Cognitive Trap Checklist:
  [X] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
      * Bukti: Bab pendahuluan murni menyajikan data statistik riil mengenai kerugian SMS spam di Indonesia tanpa menggunakan kalimat promosi yang subjektif.
  [X] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
      * Bukti: Metode CRISP-DM yang ditulis dimodifikasi khusus untuk kebutuhan preprocessing teks Indonesia (menggunakan library Sastrawi untuk stemming bahasa Indonesia).
  [X] Timeline sudah ditambah buffer 30-50% dari estimasi awal
      * Bukti: Alokasi waktu pengerjaan setiap tahapan CRISP-DM (terutama data preparation yang memakan waktu paling lama) telah disusun realistis dengan cadangan waktu pengerjaan.
  [X] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
      * Bukti: Riset tetap melakukan eksperimen penyetelan 49 kombinasi parameter yang berbeda karena ada ketidakpastian parameter mana yang akan berhasil dan menyadari model bisa saja mengalami overfitting/underfitting.
  [X] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"
      * Bukti: Hasil peningkatan akurasi (menjadi 96,94%) murni ditulis berdasarkan bukti empiris pengujian tabel parameter hasil GridSearch, bukan klaim asumsi sepihak sejak awal.

## Rubrik Self-Assessment

| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor | Justifikasi Berdasarkan Jurnal |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Koherensi** | >2 koneksi vertikal terputus | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas | **3** | *Red thread* sangat jelas mulai dari data tingginya kasus SMS spam (Problem), optimasi parameter SVM via GridSearch & Streamlit (Gap/RQ/Hypothesis), pengujian Confusion Matrix (Metric), hingga alur CRISP-DM dan skema 10-fold Cross-Validation (System/Experiment). |
| **Specificity** | Variabel/metrik masih abstrak, tidak ada angka | Sebagian metrik terdefinisi numerik | Semua metrik + threshold + unit pengukuran jelas | **3** | Semua metrik evaluasi didefinisikan secara kuantitatif melalui matriks evaluasi (*Accuracy*, *Precision*, *Recall*, *F1-Score*) dengan unit persentase (%). Angka keberhasilan terdefinisi secara presisi hingga target empiris akhir sebesar 96,94%. |
| **Feasibility** | Timeline >6 bulan tanpa memperhitungkan sumber | Timeline 3-6 bulan dengan asumsi tertentu | Timeline 1-3 bulan realistis dengan rencana detail | **3** | Siklus metodologi CRISP-DM yang digunakan terbagi ke dalam 6 tahapan terstruktur yang sangat realistis diselesaikan dalam kurun waktu 1-3 bulan karena didukung oleh dataset yang siap pakai (1.623 baris data) serta library Python open-source. |
| **Rigor** | Baseline tidak jelas atau straw man | 1-2 baseline dengan justifikasi partial | 2+ baseline SOTA + justifikasi pemilihan lengkap | **3** | Proses validasi sangat ketat (*rigorous*) karena melakukan pencarian parameter optimal menggunakan GridSearch terhadap 49 kombinasi parameter kandidat, serta divalidasi silang menggunakan metode State-of-the-Art (SOTA) berupa 10-fold Cross-Validation untuk mencegah overfitting. |

**Skor Total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> **Catatan Perbaikan:** Proposal sudah sangat matang dan siap untuk dieksekusi secara penuh karena seluruh indikator penilaian telah memenuhi kriteria "Baik" (Skor Maksimal).
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal berdasarkan dokumen "Ws01-02_DETEKSI SMS SPAM BERBAHASA INDONESIA MENGGUNAKAN.pdf".

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| **Problem Statement** | WS-02 | Indonesia merupakan negara dengan jumlah pesan SMS spam tertinggi di Asia pada tahun 2020, di mana mayoritas di antaranya berupa layanan keuangan, asuransi, promo, dan penipuan (*scam*) yang merugikan serta melanggar privasi pengguna. |
| **Gap** | WS-03 | Diperlukan suatu pemodelan text mining klasifikasi SMS spam berbahasa Indonesia yang optimal berbasis machine learning, yang kemudian diimplementasikan ke dalam aplikasi web interaktif agar dapat diuji secara langsung oleh masyarakat umum untuk pencegahan dini. |
| **RQ** | WS-04 | Bagaimana tingkat akurasi algoritma *Support Vector Machine* (SVM) dengan kombinasi ekstraksi fitur TF-IDF dan optimasi parameter *GridSearch* dalam mengklasifikasikan SMS spam berbahasa Indonesia, serta bagaimana implementasinya pada Aplikasi Deteksi berbasis Streamlit? |
| **Hipotesis** | WS-04 | $H_1$: Penerapan algoritma SVM dengan kernel *Radial Basis Function* (RBF) yang dioptimasi via *GridSearch* mampu menghasilkan akurasi klasifikasi SMS spam berbahasa Indonesia yang tinggi (mencapai $\ge 95\%$) dan berhasil diintegrasikan ke sistem Streamlit. |
| **Variabel & Metrik** | WS-05 | Independent Variable (IV) berupa variasi nilai hyperparameter C, Gamma ($\gamma$), dan pembobotan kata TF-IDF[cite: 1]. Dependent Variable (DV) diukur melalui metrik *Accuracy*, *Precision*, *Recall*, dan *F1-score* yang diturunkan dari komponen *Confusion Matrix*. |
| **Sistem** | WS-06 | Sistem dirancang menggunakan metodologi CRISP-DM yang mencakup alur *preprocessing* (Case Folding, Tokenisasi via NLTK, Stopword Removal, Stemming via Sastrawi), pembobotan TF-IDF, pemodelan SVM Scikit-Learn, dan antarmuka web berbasis Streamlit. |
| **Desain Eksperimen** | WS-07 | Eksperimen dijalankan dengan membagi dataset sebanyak 1.623 baris menjadi data latih (80%) dan data uji (20%), dilanjutkan dengan proses pelatihan 49 kombinasi parameter grid menggunakan metode validation berupa 10-fold *Cross-Validation*. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| **Problem → Gap** | ✅ | Gap untuk membangun klasifikasi teks dan aplikasi pengetesan muncul langsung dari tingginya statistik kasus kerugian akibat SMS spam di Indonesia yang terdokumentasi di literatur[cite: 1]. |
| **Gap → RQ** | ✅ | RQ secara eksplisit mempertanyakan efektivitas metode klasifikasi (SVM) beserta bentuk deployment aplikasi webnya (Streamlit) demi menutup gap solusi praktis bagi pengguna ponsel[cite: 1]. |
| **RQ → Hypothesis** | ✅ | Hipotesis $H_1$ memprediksi parameter performa spesifik (Akurasi tinggi $\ge 95\%$) dan keberhasilan fungsional dari jawaban atas pertanyaan riset yang diajukan[cite: 1]. |
| **Hypothesis → Metric** | ✅ | Variabel performa model dalam hipotesis diukur secara presisi dengan metrik matematika standar klasifikasi (*Accuracy*, *Precision*, *Recall*, *F1-score*)[cite: 1]. |
| **Metric → System** | ✅ | Komponen tahap *Evaluation* dalam siklus CRISP-DM pada sistem berfungsi menghasilkan laporan klasifikasi (*classification report*) numerik dari hasil prediksi model[cite: 1]. |
| **System → Experiment** | ✅ | Desain eksperimen menggunakan *modelling pipeline* dalam sistem untuk melatih dan mengevaluasi 49 kandidat kombinasi parameter dengan skema 10-fold *Cross-Validation*[cite: 1]. |

**Koneksi mana yang paling lemah?** Koneksi antara *Gap*  *RQ*.

**Bagaimana cara memperkuatnya?**
> Menambahkan argumen komparatif yang lebih mendalam pada bagian tinjauan pustaka mengenai keterbatasan algoritma *baseline* lain (seperti Naïve Bayes, LSTM, atau SGD Classifier) sehingga urgensi pemilihan SVM sebagai fokus utama di RQ menjadi lebih kuat dan terjustifikasi[cite: 1].

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [X] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? Istilah-istilah inti seperti "SMS Spam berbahasa Indonesia", "Support Vector Machine (SVM)", "CRISP-DM", dan "Streamlit" sudah konsisten terjaga dari penentuan masalah hingga desain eksperimen[cite: 1].

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| **Koherensi** | 3 | Alur penyusunan dari penentuan masalah SMS spam di Indonesia hingga eksekusi pemodelan menggunakan data riil mengalir secara logis, runtut, dan saling mengikat[cite: 1]. |
| **Specificity** | 3 | Target metrik kuantitatif didefinisikan secara sangat jelas menggunakan angka absolut melalui pengujian matriks evaluasi (*Confusion Matrix*)[cite: 1]. |
| **Feasibility** | 3 | Riset sangat realistis dan dapat diimplementasikan karena menggunakan dataset publik, pustaka *open-source* Python (Scikit-Learn), dan platform Streamlit yang dapat diakses gratis[cite: 1]. |
| **Rigor** | 3 | Proses pengujian model dilakukan secara ketat melalui penyetelan parameter via *GridSearch* serta divalidasi berulang menggunakan skema 10-fold *Cross-Validation*[cite: 1]. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? Proposal telah siap sepenuhnya karena seluruh komponen *Integration Map* telah saling terhubung secara kokoh dan menghasilkan akurasi akhir sebesar 96,94%.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Tahap *Business Understanding* dan penentuan rumusan masalah (WS-02), karena landasan data empiris mengenai dampak buruk dan maraknya kasus SMS spam di Indonesia sudah terekam jelas di berbagai laporan literatur.

**Bagian tersulit:** Tahap *Data Preparation* (WS-05), karena data teks tidak terstruktur bahasa Indonesia membutuhkan penanganan preprocessing yang sangat bertahap (seperti *case folding, tokenisasi, stopword removal,* dan *stemming* algoritma Nazief & Andriani via Sastrawi) agar siap dikonversi ke vektor TF-IDF.

**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, saya akan memperluas cakupan dataset dengan menambahkan variasi data teks dari platform pesan instan modern lainnya serta mencoba mengeksplorasi teknik ekstraksi fitur modern selain TF-IDF untuk dibandingkan akurasinya dengan model SVM yang sudah ada.

---

