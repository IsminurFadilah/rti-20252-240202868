# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     | SVM-RBF  | 42   | C=10, gamma=0.1, k=10  | Done   | 45s   | log_run_001.json |
| 2     | SVM-RBF  | 100  | C=10, gamma=0.1, k=10  | Done   | 43s   | log_run_002.json |
| 3     | SVM-RBF  | 2026 | C=10, gamma=0.1, k=10  | Done   | 46s   | log_run_003.json |
| 4     | SVM-RBF  | 777  | C=10, gamma=0.1, k=10  | Done   | 44s   | log_run_004.json |
| 5     | SVM-RBF  | 999  | C=10, gamma=0.1, k=10  | Done   | 45s   | log_run_005.json |

Jumlah runs per skenario : 5
Total runs               : 5

DATA LOG (per run):
  Run ID    : run-svm-rbf-001
  Timestamp : 2026-06-23T10:00:00
  Skenario  : Optimasi SVM-RBF Hyperparameter Terbaik
  Input     : 1.623 baris teks SMS berbahasa Indonesia (80% Train, 20% Test)
  Output    : Accuracy: 0.9694, Precision: 0.97, Recall: 0.95, F1-Score: 0.96
  Anomali   : Tidak ada (None)
  Catatan   : Konvergensi model tercapai dengan stabil pada seluruh lipatan Cross-Validation.
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk validasi stabilitas model SVM dengan mengunci kombinasi hyperparameter terbaik (*SOTA*) dari jurnal menggunakan 5 *random seed* berbeda untuk membuktikan *repeatability*.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | SVM Spam Detection (RBF) | 42 | C=10, gamma=0.1, Split=80:20 | Planned |
| 2 | SVM Spam Detection (RBF) | 100 | C=10, gamma=0.1, Split=80:20 | Planned |
| 3 | SVM Spam Detection (RBF) | 2026 | C=10, gamma=0.1, Split=80:20 | Planned |
| 4 | SVM Spam Detection (RBF) | 777 | C=10, gamma=0.1, Split=80:20 | Planned |
| 5 | SVM Spam Detection (RBF) | 999 | C=10, gamma=0.1, Split=80:20 | Planned |

**Total skenario:** 1 (Skenario Kombinasi Parameter Terbaik)  
**Run per skenario:** 5  
**Total run keseluruhan:** 5  

---

## Latihan 2 — Data Log Terstruktur

Format pencatatan data log eksperimen untuk menjamin transparansi *reproducibility*.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | `run-svm-001` |
| Timestamp | `2026-06-23T10:15:30` |
| Scenario Name | `SVM_RBF_GridSearch_Best` |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | `42` |
| Code version | `git commit bd7a812` |
| Hardware Environment | `Intel(R) Core(TM) i7-8565U, RAM 16GB` |
| Runtime Environment | `Python 3.12.4, scikit-learn 1.3.2` |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Accuracy | *float* | 0.0 – 1.0 (Target Jurnal: 0.9694) |
| Precision | *float* | 0.0 – 1.0 |
| Recall | *float* | 0.0 – 1.0 |
| F1-Score | *float* | 0.0 – 1.0 |
| Execution Time | *float* | > 0.0 detik |

**Format output:** [ ] CSV / [X] JSON / [ ] Database / [ ] Lainnya: ____  
*(Catatan: JSON dipilih karena fleksibel untuk menyimpan struktur metadata konfigurasi gabungan tipe teks dan angka).*

---

## Latihan 3 — Anomaly Protocol

Rencana penanganan anomali operasional selama proses eksekusi kode dijalankan pada laptop Intel i7 milikmu.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | `ModuleNotFoundError` pada library Sastrawi akibat isu *compatibility* di Python 3.12.4 | Dokumentasikan pesan kesalahan, perbaiki struktur impor atau gunakan lingkungan virtual (*venv*) yang bersih, lalu jalankan ulang. |
| Hasil ekstrem | Akurasi mendadak anjlok ke < 50% atau melonjak 100% (*overfitting* parah) | Selidiki kebocoran data (*data leakage*) pada tahap pembagian data teks TF-IDF. Dokumentasikan nilai seed yang memicu, jangan hapus log. |
| Waktu eksekusi anomali | Eksekusi GridSearch memakan waktu > 10 menit (biasanya hanya ~45 detik) | Periksa apakah laptop mengalami *thermal throttling* atau ada proses latar belakang (*background process* Windows) yang berat. Catat suhu perangkat, dinginkan, lalu uji ulang. |
| Inkonsistensi dengan run lain | Hasil akurasi antar-seed melonjak fluktuatif (misal selisih > 5%) | Investigasi apakah distribusi label *spam* dan *normal* pada *subset* data latih tidak seimbang akibat fungsi `stratify=y` lupa diaktifkan. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Apakah Anda pernah melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, dalam pengerjaan tugas-tugas pemrograman atau praktikum berskala kecil sebelumnya, saya sering kali hanya melakukan *single run*. Begitu kode berjalan lancar tanpa *error* dan memunculkan satu nilai angka akurasi di terminal, saya langsung mengambil angka tersebut sebagai hasil akhir laporan. Risikonya adalah angka tersebut bisa jadi merupakan "keberuntungan statistik" semata (*cherry-picked result*) akibat pembagian *dataset* kebetulan mengelompokkan data yang mudah ditebak oleh model.

**Yang akan dilakukan berbeda:**
> Mulai sekarang, saya akan mengunci komponen *random seed* (seperti `random_state=42`) di setiap tingkat pustaka kode Python dan mengadopsi skema pengujian *multiple run* (minimal 5 kali eksekusi dengan variasi benih acak terencana). Dengan *multiple run*, tingkat kepercayaan sains dalam proposal ini meningkat drastis karena saya dapat menyajikan nilai rata-rata (*mean*) dan standar deviasi yang membuktikan bahwa performa deteksi spam akurasi 96,94% tersebut benar-benar konsisten dan dapat direproduksi oleh siapa pun, kapan pun, dan di laptop mana pun.