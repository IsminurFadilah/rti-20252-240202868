# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Bagaimana tingkat akurasi algoritma Support Vector Machine (SVM) dengan pembobotan Term Frequency-Inverse Document Frequency (TF-IDF) dalam mengklasifikasikan SMS spam berbahasa Indonesia?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|Kombinasi Hyperparameter SVM| IV   |Variasi nilai parameter penalti dan parameter kelengkungan kernel RBF untuk mencari batas keputusan (hyperplane) paling optimal.|Pasangan koordinat grid|Nominal|-|Menguji daftar matriks kombinasi nilai C dan gamma [0.001, 0.01, 0.1, 1, 10, 100, 1000] melalui GridSearchCV hingga ditemukan nilai terbaik yaitu C = 10 dan gamma = 1| Parameter C (mengontrol sanksi kesalahan klasifikasi) dan gamma (mengontrol pengaruh sampel data latih)  sangat penting agar model tidak mengalami overfitting atau underfitting|
|Kinerja Klasifikasi Model| DV   |Tingkat keandalan dan keakuratan model dalam mendeteksi dan memisahkan pesan SMS normal (ham) dari SMS penipuan/promo (spam).|Accuracy, Precision, Recall, dan F1-Score |Ratio|% (Persentase)|Menguji performa model terbaik hasil tuning pada 20% data uji (325 data) , memetakan hasilnya ke Confusion Matrix , lalu dikalkulasi menggunakan library scikit-learn untuk menghasilkan akurasi final 96,94%|Metrik ini merupakan standar universal evaluasi klasifikasi. Nilai Precision dan F1-Score wajib diukur untuk menjamin sangat minimnya pesan penting/normal yang salah terblokir (False Positive)|
|Arsitektur Pemrosesan Teks & Dataset| CV   |Kondisi lingkungan eksperimen teks, urutan pembersihan data, serta sumber basis data yang dikunci seragam selama eksperimen dijalankan|Dataset Yudi Wibisono (1623 baris) dan urutan Pipeline Preprocessing yang dikunci tetap.|Nominal|- |Menyatukan semua langkah pembersihan teks dan penilaian kata ke dalam satu jalur proses yang otomatis dan tidak bisa diubah-ubah|Pembatasan parameter ini wajib dilakukan agar fluktuasi atau perubahan nilai akurasi (DV) murni terjadi akibat pengaruh optimasi hyperparameter SVM (IV), bukan karena perubahan penanganan data teks|




Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:**Bagaimana tingkat keakuratan algoritma Support Vector Machine (SVM) dengan pembobotan TF-IDF dalam mengklasifikasikan SMS spam berbahasa Indonesia?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| **Kombinasi Nilai Parameter ($C$ dan $\gamma$)** | IV | Pengaturan tingkat ketegasan model dan kelengkungan garis pemisah data. | Pasangan angka nilai $C$ dan $\gamma$ (Contoh hasil terbaik: $C=10, \gamma=1$) | Nominal | — |
| **Kinerja Klasifikasi Model** | DV | Seberapa tepat dan akurat model dalam membedakan SMS asli dan SMS spam. | Nilai persentase *Accuracy*, *Precision*, *Recall*, dan *F1-Score* | Ratio | % |
| **Aturan Pembersihan Teks & Dataset** | CV | Alur standar mencuci teks dan sumber data teks yang dibuat sama/tetap. | Dataset Yudi Wibisono (1623 data) & Jalur proses otomatis (*Pipeline*) | Nominal | — |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| **Representative** | 5 | *Accuracy* (96,94%) sangat cocok karena jumlah data antara SMS spam (829 data) dan SMS asli (794 data) di dalam dataset ini seimbang (*balanced dataset*). |
| **Sensitive** | 4 | Metrik ini sangat peka karena nilainya langsung berubah naik atau turun setiap kali kita mengubah kombinasi angka parameter $C$ dan $\gamma$. |
| **Feasible** | 5 | Sangat mudah didapatkan karena kode program untuk menghitungnya sudah otomatis tersedia langsung di dalam library python (*Scikit-Learn*). |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> **Jika ya, apa dan mengapa?** Perlu metrik pendukung yaitu *Precision* dan *F1-Score*. Tujuannya agar bisa memastikan bahwa sistem tidak mudah salah tebak, seperti memblokir SMS penting/asli dari keluarga/lainnya yang dikira sebagai SMS spam (*False Positive*).

**Contoh kasus ceiling effect untuk metrik ini:**
> Terjadi ketika nilai akurasi pada data latih (*Training Accuracy*) sudah mentok mencapai skor sempurna **100%**. 

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| **Completeness** | *Apakah semua data point terkumpul?* | Ya, seluruh 1623 data SMS memiliki teks pesan dan label kategori yang lengkap. | Melakukan pengecekan otomatis dengan program untuk memastikan tidak ada baris data yang kosong (*missing values*). |
| **Consistency** | *Apakah ada kontradiksi internal?* | Ada risiko teks pesan yang mirip tetapi dilabeli berbeda karena pembagian kategori awal yang bercabang. | Menyatukan semua label penipuan dan promo ke dalam satu nama kategori yang konsisten, yaitu "Spam". |
| **Validity** | *Apakah benar-benar mengukur yang dimaksud?* | Ya, semua data berisi pesan teks asli dalam format SMS berbahasa Indonesia. | Membersihkan data dari baris yang duplikat (pesan yang sama persis) agar data yang diuji benar-benar unik. |
| **Representativeness** | *Apakah sampel mewakili populasi target?* | Ya, teks dalam dataset sudah berisi kata-kata khas penipuan dan promo yang sering beredar di Indonesia. | Memastikan kata kunci seperti "hadiah", "selamat", "pinjam", "klik link" terekstraksi dengan baik pada tahap TF-IDF. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik evaluasi setelah melihat hasil data eksperimen dianggap sebagai kecurangan ilmiah (*p-hacking*) karena peneliti sengaja mencari-cari dan hanya menampilkan metrik yang hasilnya kelihatan bagus/sukses demi mendukung dugaannya, sementara metrik yang hasilnya jelek sengaja disembunyikan. Hal ini membuat hasil penelitian menjadi tidak jujur dan tidak objektif.

> Bedanya dengan eksplorasi data yang sah (*Exploratory Data Analysis*) adalah eksplorasi dilakukan di **awal sekali** sebelum model dibuat. Tujuannya murni untuk berkenalan dengan karakteristik data (seperti melihat kata apa yang paling sering muncul atau melihat berapa jumlah data spam), bukan untuk mengutak-atik tolak ukur penilaian akhir yang seharusnya sudah dikunci sejak awal eksperimen dirancang.