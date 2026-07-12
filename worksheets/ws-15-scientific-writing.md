# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Analisis Komparatif Performa SVM dan Naive Bayes dalam Klasifikasi SMS Spam
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi
  [x] Introduction — konteks (spam), gap (efisiensi vs akurasi), RQ, kontribusi
  [x] Related Work — teknik NLP, komparasi algoritma, gap positioning
  [x] Method — preprocessing (Sastrawi), ekstraksi fitur (TF-IDF), skenario eksperimen
  [x] Results — tabel perbandingan akurasi, grafik error bar
  [x] Discussion — interpretasi hasil, analisis kegagalan, batasan
  [x] Conclusion — jawaban RQ, implikasi, riset lanjutan

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — mudah dipahami tanpa re-read
  [X] Precision — tidak ada istilah ambigu
  [X] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama | Target Kata |
|---------|---------------------------|------------|
| Abstract | Deteksi SMS spam penting untuk keamanan pengguna. SVM dan Naive Bayes dibandingkan performanya menggunakan dataset SMS. Hasil: SVM mencapai 94% akurasi. | 200 |
| Introduction | Masalah spam yang mengganggu. Gap: kebutuhan filter ringan namun efektif untuk perangkat mobile. RQ: Bagaimana efektivitas SVM vs NB? | 600 |
| Related Work | Review teknik *text mining* dan klasifikasi biner pada pesan singkat. | 800 |
| Method | Dataset prep, TF-IDF, SVM (linear) vs NB, k-fold cross validation. | 1000 |
| Results | Tabel akurasi, presisi, recall, F1-Score, dan durasi latih. | 600 |
| Discussion | Analisis mengapa hasil tidak signifikan secara statistik (p > 0.05). | 700 |
| Conclusion | Ringkasan temuan: kedua algoritma efektif, saran model yang lebih adaptif. | 300 |
---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|   | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 (SVM vs NB) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik (Accuracy) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Var (Teks SMS) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Klaim (Efektif) | ✓ | ✓ | ✓ | ✓ | ✓ |

**Inkonsistensi yang ditemukan:** Tidak ada inkonsistensi.
**Tindakan perbaikan:** N/A

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> "Penelitian ini memakai SVM dan NB untuk SMS spam. Hasilnya SVM sedikit lebih bagus tapi bedanya tipis saja secara statistik. Jadi keduanya bisa dipakai sebenarnya."

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Terlalu santai/bahasa lisan | Gunakan istilah teknis formal |
| Precision | Tidak spesifik (bagus/tipis) | Sertakan angka (94% vs 93%) |
| Conciseness | Ada kalimat redundan | Gabungkan kalimat efektif |

**Paragraf setelah perbaikan:**
> "Penelitian ini mengevaluasi kinerja algoritma Support Vector Machine (SVM) dan Naive Bayes dalam mendeteksi SMS spam. Hasil eksperimen menunjukkan bahwa SVM mencapai akurasi 94%, sedangkan Naive Bayes mencapai 93%. Analisis statistik mengindikasikan bahwa perbedaan performa kedua model tidak signifikan secara statistik (p > 0.05), sehingga keduanya merupakan alternatif yang valid untuk implementasi praktis."

---

## Refleksi

> **Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset?**
> Menulis "tentang" riset hanya mendeskripsikan apa yang saya lakukan (seperti laporan kegiatan). Menulis sebagai "argumen" riset adalah membangun alur logika yang meyakinkan pembaca mengapa metode saya relevan, mengapa hasil saya kredibel, dan mengapa temuan saya penting bagi bidang ilmu tersebut.

> **Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?**
> Urutan ini membuat tulisan lebih koheren. Dengan menulis Method/Results terlebih dahulu, saya mendapatkan "bukti" sebelum saya membuat "klaim" di Introduction. Ini mencegah *overselling* (klaim berlebihan) dan membuat alur argumen menjadi jauh lebih kuat.
