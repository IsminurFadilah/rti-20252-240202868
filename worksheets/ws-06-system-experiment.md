# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Bagaimana tingkat keakuratan algoritma SVM dengan pembobotan TF-IDF dalam menyaring SMS spam berbahasa Indonesia?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| **Kombinasi Hyperparameter** | IV | Daftar pilihan angka parameter (`param_grid`) untuk dicoba mesin. | Mengubah-ubah isi angka sanksi kesalahan (C) dan kelengkungan garis (gamma) pada skrip kode Python. |
| **Kinerja Klasifikasi Model** | DV | Fungsi pencetak skor hasil tebakan model (`classification_report`). | Sistem otomatis menghitung berapa persen SMS yang berhasil ditebak dengan benar (Akurasi). |
| **Aturan Pembersihan Teks & Dataset** | CV | Alur pabrik otomatis (`Pipeline`) yang mengikat urutan kerja program. | Mengunci urutan pembersihan teks dan jumlah data agar selalu sama dari awal sampai akhir tes. |

4 Prinsip Desain:
  [X] Traceability — Setiap bagian program punya tugas yang jelas sesuai variabelnya.
  [X] Variable Isolation — Mengubah angka parameter ($C$ dan $\gamma$) tidak akan merusak atau mengubah cara membersihkan teks.
  [X] Measurement Integration — Kode untuk menghitung akurasi sudah terpasang otomatis tepat setelah mesin selesai belajar.
  [X] Reproducibility — Pembagian data dikunci agar kalau program dijalankan ulang, hasilnya tetap sama dan konsisten.

Experimental Setup:
  Input data     : 1623 baris teks SMS asli orang Indonesia (ada yang spam, ada yang normal).
  Parameter      : Data dibagi (80% buat belajar, 20% buat tes), pencarian rumus diulang 10 kali (10-fold CV).
  Output format  : Catatan angka parameter paling pintar, persentase akurasi, dan file jadi berformat `.pkl` (Pickle).

---

## Latihan 1 — Variable-to-Component Mapping

**RQ:** Bagaimana tingkat keakuratan algoritma SVM dengan pembobotan TF-IDF dalam menyaring SMS spam berbahasa Indonesia?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| **Kombinasi Hyperparameter** | IV | Fitur pencari setelan terbaik (`GridSearchCV`). | Mengganti isi daftar angka parameter C dan gamma yang mau diuji. |
| **Kinerja Klasifikasi Model** | DV | Fungsi hitung skor otomatis (`model.score`). | Menampilkan hasil akhir ketepatan tebakan dalam bentuk persen (%). |
| **Aturan Pembersihan Teks & Dataset** | CV | Fungsi pembagi data (`train_test_split`). | Mengunci perbandingan data belanjaan dan ujian tetap di angka 80:20. |

**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| **Traceability** | ✅ Aman | Alurnya jelas dan urut: SMS masuk rightarrow dicuci bersih rightarrow dinilai katanya rightarrow ditebak SVM rightarrow keluar skor akurasi. |
| **Modularity** | ✅ Aman | Menggunakan fitur `Pipeline`. Bagian untuk mencuci teks dipisah rapi dan tidak campur aduk dengan bagian mesin tebak SVM. |
| **Controllability** | ✅ Aman | Semua setelan penting (seperti putaran ujian sebanyak 10 kali) diatur di satu tempat terpusat, tidak tersebar berantakan. |
| **Measurability** | ✅ Aman | Begitu ujian data selesai, program langsung otomatis menampilkan tabel hasil tebakan (*Confusion Matrix*) ke layar. |

**Prinsip mana yang paling sulit dipenuhi?** *Controllability*

**Strategi untuk mengatasinya:**
> Mengumpulkan semua setelan angka di bagian paling atas kode program, supaya kalau mau mengubah sesuatu tidak perlu repot mencari di sela-sela baris kode yang panjang.

---

## Latihan 3 — Ablation Study Planning

Ablation study ini intinya adalah eksperimen "bongkar pasang" fitur untuk melihat fitur mana yang paling bikin mesin jadi pintar.

| Kondisi | Komponen A (Dicuci Bersih) | Komponen B (Hitung 2 Kata) | Komponen C (Garis Melengkung RBF) | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| **Full** | ✅ Aktif | ✅ Aktif | ✅ Aktif | Ini setelan terbaik. Mesin paling pintar dengan akurasi tebakan mencapai **96,94%**. |
| **– A** | ❌ Matikan (SMS kotor langsung diproses) | ✅ Aktif | ✅ Aktif | Akurasi turun karena mesin bingung dengan huruf besar-kecil atau kata singkatan yang berantakan. |
| **– B** | ✅ Aktif | ❌ Matikan (Hitung per 1 kata saja) | ✅ Aktif | Akurasi sedikit turun karena mesin kehilangan arti dari gabungan dua kata penting (seperti "pinjam uang"). |
| **– C** | ✅ Aktif | ✅ Aktif | ❌ Matikan (Pakai garis lurus biasa) | Akurasi anjlok parah karena pola kata SMS penipuan terlalu acak dan tidak bisa dipisah pakai garis lurus sederhana. |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen C (Garis Melengkung RBF)

**Mengapa?**
> Karena pola SMS spam di Indonesia sangat rumit dan kata-katanya mirip dengan SMS asli. Tanpa bantuan rumus garis melengkung (Kernel RBF), mesin SVM bakal kesusahan bikin batas pembatas yang pas untuk memisahkan SMS penipuan dan SMS normal.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risikonya adalah kalau dari awal kita sudah sibuk bikin tampilan web Streamlit yang bagus, tombol visual, dan fitur produk lainnya sebelum mesinnya diuji, kita bakal pusing sendiri kalau hasil akurasinya jelek. Kita jadi tidak tahu apakah yang bikin jelek itu karena rumus SVM-nya salah, cara mencuci teksnya keliru, atau malah ada eror di tombol webnya.
 
> Makanya, arsitektur modular (sistem yang dipisah per bagian seperti kotak lego) sangat penting untuk penelitian. Kita jadi bisa fokus menguji kecerdasan mesinnya dulu secara adil, gampang membongkar pasang fitur untuk dicoba, dan memastikan kalau peneliti lain meniru program kita, mereka akan mendapatkan hasil akurat yang sama persis.
