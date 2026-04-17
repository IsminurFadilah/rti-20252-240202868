# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Ismi Nur Fadilah
Tanggal          : 12 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana metode pengujian dilakukan dan apakah dataset yang digunakan cukup representatif?
   - Data yang dibutuhkan untuk verifikasi: Dataset SMS yang digunakan, metode evaluasi, serta hasil confusion matrix atau akurasi

2. Posisi paradigma:
   - Pendekatan: [✓] Positivis  [ ] Interpretivis  [✓] Design Science  [ ] Mixed
   - Alasan: Penelitian ini menggunakan data kuantitatif untuk mengukur akurasi klasifikasi serta membangun sistem sebagai alat pengujian

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Semua kata tertentu pasti menunjukkan spam
   - Sumber bias potensial: Dataset hanya dari jenis SMS tertentu (promo saja)
   - Langkah mitigasi: Menggunakan dataset yang beragam dan melakukan validasi data

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data SMS dan hasil klasifikasi
   - Batasan yang diakui sejak awal: Sistem hanya mendeteksi berdasarkan pola teks sederhana
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Deteksi SMS Spam Berbahasa Indonesia Menggunakan Algoritma Support Vector Machine 
> Penulis (Tahun): Mohamad Arif Sofyan, Nining Rahaningsih, Raditya Danar Dana (2024)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data SMS spam dan non-spam | Data tidak mewakili semua jenis SMS di Indonesia |
| Data → Processing | Membersihkan teks (menghapus simbol, stopword, dll) | Informasi penting bisa hilang saat preprocessing |
| Processing → Analysis | Melatih model SVM untuk klasifikasi | Parameter model tidak optimal |
| Analysis → Inference | Menyimpulkan model mampu mendeteksi spam dengan baik | Tidak mempertimbangkan kondisi data lain |
| Inference → Knowledge | Menyatakan metode efektif secara umum | Generalisasi berlebihan |

**Distorsi paling besar di tahap:** Data → Processing

**Dua distorsi spesifik yang teridentifikasi:**
1. Dataset tidak mewakili seluruh variasi SMS spam di dunia nyata 
2. Proses preprocessing dapat menghilangkan kata penting yang mempengaruhi hasil klasifikasi

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus melaporkan hasil dengan dan tanpa outlier |
| Transparansi | Peneliti wajib menjelaskan alasan penghapusan data |
| Peer review | Reviewer dapat mengevaluasi apakah ada manipulasi data |

**Keputusan akhir dan justifikasi:**
> Peneliti tidak boleh menghapus data outlier hanya untuk mendapatkan hasil yang signifikan. Semua hasil harus dilaporkan agar penelitian tetap objektif, transparan, dan dapat dipercaya.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Deteksi SMS spam berbahasa Indonesia menggunakan metode klasifikasi

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 2 | 4 |
| Jenis data yang dikumpulkan | Data teks SMS dan hasil klasifikasi | Persepsi pengguna | Sistem deteksi spam |
| Limitasi paradigma | Tidak mempertimbangkan konteks sosial |  Subjektif| Fokus pada artefak sistem |

**Paradigma yang dipilih:** Positivis
**Alasan:** Penelitian ini berfokus pada pengukuran akurasi sistem secara objektif menggunakan data dan metode statistik, sehingga sesuai dengan paradigma positivis.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum memahami materi ini, saya cenderung langsung percaya pada klaim seperti “95% akurat” tanpa mempertanyakan bagaimana data diperoleh dan diuji. Setelah memahami adanya kemungkinan distorsi dalam setiap tahap penelitian, saya akan lebih kritis dengan menanyakan sumber data, metode pengujian, serta validitas hasil sebelum mempercayai klaim dalam sebuah paper.