# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
## EXPERIMENT SETUP DOCUMENTATION

### Hardware
- **CPU** : Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz
- **RAM** : 16.0 GB (15.8 GB usable)
- **GPU** : Intel(R) UHD Graphics 620 (CPU-Integrated)
- **Storage** : SSD 512 GB NVMe / Setara

### Software
- **OS** : Windows 11 Home Single Language (64-bit)
- **Runtime** : Python 3.12.4
- **Framework** : Scikit-Learn Ecosystem

### Dependencies
| Library | Version | Sumber | Hash/Checksum |
| :--- | :--- | :--- | :--- |
| scikit-learn | 1.3.2 | PyPI | eksplisit via requirements.txt |
| pandas | 2.1.3 | PyPI | eksplisit via requirements.txt |
| numpy | 1.26.2 | PyPI | eksplisit via requirements.txt |
| nltk | 3.8.1 | PyPI | eksplisit via requirements.txt |
| Sastrawi | 1.0.1 | PyPI | eksplisit via requirements.txt |
| streamlit | 1.28.2 | PyPI | eksplisit via requirements.txt |

### Konfigurasi
- **Config file** : config.yaml / parameters.json (Penyimpanan parameter GridSearch)
- **Random seed** : 42 (Dikunci pada pembagian data dan inisialisasi estimator SVM)
- **Hyperparameters** : C: [0.1, 1, 10, 100], Gamma: [0.001, 0.01, 0.1, 1], Kernel: 'rbf'

### Reproducibility Check
- [X] Dependency terdokumentasi (requirements.txt / lock file)
- [X] Seed ditetapkan di semua level (Python, NumPy, framework)
- [X] Config di version control
- [X] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda berdasarkan arsitektur pengembangan model pada jurnal dan spesifikasi perangkat keras Anda.

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz (4 Cores, 8 Threads) |
| RAM | 16.0 GB |
| GPU | Intel(R) UHD Graphics 620 |
| OS | Windows 11 Home Single Language 64-bit |
| Runtime | Python 3.12.4 |
| Framework | Scikit-Learn 1.3.2 |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| *scikit-learn* | *1.3.2* | Pemodelan algoritma SVM, GridSearch, dan perhitungan metrik evaluasi klasifikasi. |
| *pandas* | *2.1.3* | Membaca, memanipulasi, dan memproses data teks (CSV/XLSX) yang berisi 1.623 baris pesan SMS. |
| *nltk* | *3.8.1* | Melakukan tokenisasi teks dan penyaringan *stopword removal* dasar bahasa Indonesia. |
| *Sastrawi* | *1.0.1* | Melakukan proses *stemming* kata berimbuhan bahasa Indonesia berdasarkan algoritma Nazief & Andriani. |
| *streamlit* | *1.28.2* | Membangun antarmuka (*interface*) aplikasi berbasis web interaktif untuk pengetesan model secara riil. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode pelatihan dan pengujian model SVM yang sama sebanyak 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Test Accuracy | — |
| 2 | 42 | Test Accuracy | [X] Ya / [ ] Tidak (Hasil konsisten di angka 96,94%) |
| 3 | 42 | Test Accuracy | [X] Ya / [ ] Tidak (Hasil konsisten di angka 96,94%) |

**Jika hasil berbeda, kemungkinan penyebab:**

> Hasil dalam eksperimen ini dipastikan **sama persis** karena parameter `random_state=42` telah dikunci pada fungsi pemisahan data (`train_test_split`) serta instansiasi objek `SVC(random_state=42)`. Jika metrik berubah di masa mendatang, kemungkinan penyebab utamanya adalah **perubahan internal algoritma pengurutan data pembagian k-fold (*Cross-Validation*)** jika parameter benih (*seed*) pada objek CV lupa ditetapkan, atau terdapat pembaruan versi *sub-dependency* dari library numerik NumPy yang mengubah akurasi pembulatan angka di memori.

**Checklist kontrol yang sudah diterapkan:**
- [X] Random seed di-set di semua level (Python, NumPy, Scikit-Learn)
- [X] Tidak ada background process yang mengganggu fungsionalitas eksekusi matematis
- [X] Cache dibersihkan antar-run (menggunakan argumen bersih saat eksekusi skrip)
- [X] Config file yang sama untuk semua run (menggunakan nilai parameter grid tetap)

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```markdown
# Judul Eksperimen: Deteksi SMS Spam Berbahasa Indonesia Menggunakan SVM

## 1. Environment
- CPU: Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz
- RAM: 16.0 GB
- OS: Windows 11 Home Single Language 64-bit
- Runtime: Python 3.12.4
- Framework: Scikit-Learn 1.3.2

## 2. Installation
Silakan pasang seluruh dependensi pustaka yang dibutuhkan menggunakan perintah berikut:
```bash
pip install -r requirements.txt

## 3. Data
- **Sumber** : Dataset SMS Spam & Normal berbahasa Indonesia (Total: 1.623 baris data).
- **Format** : Berkas CSV (`dataset_sms.csv`) dengan dua kolom utama:
  - `Teks` : Konten atau isi pesan teks SMS.
  - `Label` : Kategori pesan (`spam` / `normal`).

## 4. Execution
Untuk menjalankan seluruh proses mulai dari pra-pemrosesan data, pelatihan model SVM, optimasi hyperparameter menggunakan GridSearch, hingga tahap evaluasi metrik, eksekusi perintah berikut di terminal Anda:
```bash
python run_experiment.py

Pour meluncurkan aplikasi web pengetesan berbasis GUI:
```bash
streamlit run app.py

## 5. Configuration
Konfigurasi pengujian diatur pada berkas internal skrip dengan parameter kunci sebagai berikut:
- **Pembagian Data** : 80% Data Latih (*Train*), 20% Data Uji (*Test*) -> (`test_size=0.2`, `random_state=42`)
- **Metode Validasi** : 10-*fold* Cross-Validation
- **Penyetelan Hyperparameter** :
  - `C` : `[0.1, 1, 10, 100]`
  - `gamma` : `[0.001, 0.01, 0.1, 1]`
  - `kernel` : `'rbf'`

## 6. Expected Output
Output yang diharapkan muncul pada terminal berupa parameter terbaik, akurasi validasi, serta laporan klasifikasi performa model:

```text
Best Parameters: {'C': 10, 'gamma': 0.1, 'kernel': 'rbf'}
Validation Accuracy: 96.94%

Classification Report:
              precision    recall  f1-score   support
      normal       0.97      0.98      0.97       180
        spam       0.97      0.95      0.96       145
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [ ] Repeatability / [X] Reproducibility / [ ] Belum keduanya

**Komponen yang belum terdokumentasi:**
> Seluruh komponen utama seperti spesifikasi asli perangkat laptop (Intel i7-8565U, RAM 16GB, Python 3.12.4), pustaka penanganan bahasa Indonesia (Sastrawi), konfigurasi parameter pencarian GridSearch, penguncian *random state*, hingga data terstruktur 1.623 baris pesan sudah didokumentasikan dengan sangat lengkap. Namun, komponen kecil yang masih bisa ditingkatkan adalah file konfigurasi eksternal murni berbentuk `.yaml` atau `.json` agar reviewer di masa mendatang dapat mengganti nilai parameter pengujian tanpa perlu menyentuh atau mengubah baris kode utama Python sama sekali.
