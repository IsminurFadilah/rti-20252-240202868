# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Bagaimana tingkat keakuratan algoritma SVM dengan pembobotan TF-IDF dalam menyaring SMS spam berbahasa Indonesia?
Hypothesis        : Penggunaan hyperparameter optimal (C=10, gamma=1) pada model SVM dapat menghasilkan akurasi penyaringan SMS spam di atas 95%.
Tipe Eksperimen   : [ ] Comparison  [ ] Ablation  [X] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Model SVM yang berjalan menggunakan setelan parameter bawaan asli pabrik (*default*). | `C=1.0`, `gamma='scale'` | Dataset Yudi Wibisono (1623 data), pembagian data 80:20, pembersihan teks + TF-IDF (1-2 kata). |
| Treatment | Model SVM yang dipasangi setelan nilai kombinasi terbaik hasil pencarian sistem. | `C=10`, `gamma=1` | Dataset Yudi Wibisono (1623 data), pembagian data 80:20, pembersihan teks + TF-IDF (1-2 kata). |

Fairness Checklist:
  [X] Dataset identik untuk semua kondisi (Sama-sama diuji pakai data Yudi Wibisono)
  [X] Preprocessing setara (Sama-sama lewat alur pencucian teks yang dikunci di Pipeline)
  [X] Tuning effort setara (Sama-sama dievaluasi lewat proses iterasi yang adil)
  [X] Environment identik (Sama-sama dijalankan di skrip Python dan komputer yang sama)
  [X] Metrik evaluasi sama (Sama-sama diukur pakai skor Akurasi, Presisi, Recall, dan F1-Score)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Kebocoran data (*data leakage*) akibat pemisahan data latih dan data uji yang tumpang tindih. | Mengunci pembagian data secara ketat menggunakan fungsi `train_test_split` dengan `random_state`. |
| External    | Model hanya jago menebak data di lab saja, tetapi jeblok saat mendeteksi SMS asli di dunia nyata. | Menggunakan dataset yang berisi pola kalimat SMS penipuan riil yang sering beredar di masyarakat Indonesia. |
| Construct   | Metrik penilaian menipu, misal akurasi kelihatan tinggi padahal model sering melewatkan SMS spam. | Menggabungkan metrik Akurasi dengan *Precision*, *Recall*, dan *F1-Score* agar penilaian performa seimbang. |
| Conclusion  | Kesimpulan hasil pengujian bias atau kebetulan karena jumlah putaran tes yang terlalu sedikit. | Menggunakan metode *10-Fold Cross-Validation* (mengulang dan mengacak ujian sebanyak 10 kali putaran). |

Statistical Plan:
  Uji statistik   : Deskriptif Komparatif & K-Fold Cross-Validation Score
  Justifikasi      : Membandingkan secara langsung nilai rata-rata persentase akurasi model sebelum dan sesudah dipasangi parameter terbaik.
  Alpha            : — (Tidak menggunakan uji hipotesis p-value tradisional)
  Effect size min  : Kenaikan akurasi minimal 2% dari model standar.

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana tingkat keakuratan algoritma SVM dengan pembobotan TF-IDF dalam menyaring SMS spam berbahasa Indonesia?
**Tipe eksperimen:** [ ] Comparison / [ ] Ablation / [X] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Menguji performa awal model SVM menggunakan parameter standar bawaan program. | `C=1.0`, `gamma='scale'` | Dataset 1623 baris data, pembagian data 80:20, pembersihan teks otomatis. |
| Treatment | Menguji performa model SVM sesudah ditala mencari nilai paling pas lewat GridSearchCV. | `C=10`, `gamma=1` | Dataset 1623 baris data, pembagian data 80:20, pembersihan teks otomatis. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ Fair | Kedua kondisi sama-sama menguji data SMS dari sumber yang sama (Dataset Yudi Wibisono). |
| Preprocessing setara | ✅ Fair | Kedua kondisi melewati mesin pencuci teks yang sama persis di dalam struktur Pipeline. |
| Tuning effort setara | ✅ Fair | Kedua model diberi kesempatan belajar dan diuji dari kantong data latih yang sama. |
| Environment identik | ✅ Fair | Seluruh tes dijalankan pada satu komputer dan versi library Python (Scikit-Learn) yang sama. |
| Metrik evaluasi sama | ✅ Fair | Hasil akhir sama-sama dinilai menggunakan rumus hitung *Confusion Matrix*. |

**Ada yang tidak fair?** [ ] Ya / [X] Tidak

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| **Internal** | Model tidak sengaja "mengintip" kunci jawaban data ujian saat proses latihan berjalan (*overfitting*). | Memisahkan data uji (20%) sejak awal dan tidak boleh disentuh selama proses pencarian parameter terbaik. |
| **External** | Kumpulan data SMS yang dipakai sudah usang, sehingga model gagal mengenali modus operandi SMS spam jenis baru. | Menggunakan dataset lokal Indonesia yang variasi teks penipuannya dinamis (berisi info hadiah, pinjol, dan promo). |
| **Construct** | Salah mengartikan arti akurasi tinggi, padahal modelnya cacat karena sering salah blokir SMS asli dari keluarga. | Menjadikan metrik *Precision* sebagai tolak ukur utama agar kasus salah memblokir SMS penting bisa dicegah. |
| **Conclusion** | Nilai akurasi tinggi 96,94% terjadi hanya karena faktor kebetulan saat pembagian data secara acak. | Menggunakan teknik pengulangan tes 10 kali (*10-fold Cross-Validation*) untuk membuktikan kestabilan model. |

**Ancaman mana yang paling sulit dimitigasi?** *External Validity*
**Mengapa?**
> Karena bahasa gaul, singkatan, dan modus penipuan lewat SMS di Indonesia selalu berubah-ubah setiap waktu. Model yang kita latih hari ini mungkin sangat pintar, tetapi bisa saja akurasinya sedikit menurun di masa depan jika komplotan penipu membuat pola kalimat baru yang belum pernah dipelajari oleh model kita.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. **Apakah perbandingannya sudah adil (*fair*)?** (Jangan-jangan metode baru diberi keuntungan dengan dibersihkan datanya secara maksimal dan dicari parameternya sampai optimal, sedangkan metode lama sengaja dibiarkan berjalan dengan setelan bawaan pabrik yang seadanya).
2. **Apakah dataset yang dipakai untuk menguji itu sama?** (Kita harus memastikan semua metode diuji menggunakan bahan baku data, porsi pembagian data, dan kondisi lingkungan eksperimen yang benar-benar identik).
3. **Metrik apa yang dipakai untuk mengklaim kemenangan tersebut?** (Apakah hanya pamer keunggulan di metrik Akurasi saja, atau metrik penting lain seperti *Precision* dan *F1-Score* juga ikut naik secara seimbang tanpa ada yang dikorbankan).