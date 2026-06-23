# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `09-docs/tahap-N-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-03-31 s.d. 2026-04-06 | Tahap 1 (WS-01 & WS-02) | Pertemuan pertama kuliah; penjelasan tata cara riset replikasi oleh Dosen; pemilihan naskah jurnal acuan klasifikasi teks SMS Spam. | [01-proposal/README.md](../01-proposal/README.md) |
| 2026-04-13 s.d. 2026-04-20 | Tahap 1 (WS-03 & WS-04) | Studi literatur mendalam terkait teori *Support Vector Machine* (SVM) dan penyusunan proposal awal replikasi model. | [02-literatur/README.md](../02-literatur/README.md) |
| 2026-04-27 s.d. 2026-05-11 | Tahap 2 (WS-05 & WS-06) | Pengumpulan data pesan, proses pembersihan duplikasi teks (*data cleaning*), hingga terbentuk dataset terstruktur 1.623 baris kalimat. | [04-data/dataset_sms.csv](../04-data/dataset_sms.csv) |
| 2026-05-18 s.d. 2026-06-01 | Tahap 3 (WS-07 & WS-08) | Praktikum pengodean pra-pemrosesan teks: *case folding*, tokenisasi, *stopword removal* (NLTK), dan *stemming* bahasa Indonesia via `Sastrawi==1.0.1`. | [05-kode/preprocessing.py](../05-kode/preprocessing.py) |
| 2026-06-08 | Tahap 4 (WS-09) | Pembagian proporsi data train/test (80:20); ekstraksi dan pembobotan fitur kata dengan TF-IDF; dokumentasi spesifikasi kontrol lingkungan (`Python 3.13.7`). | [09-docs/tahap-4-optimasi-model.md](../09-docs/tahap-4-optimasi-model.md) |
| 2026-06-15 s.d. 2026-06-23 (Minggu ke-13) | Tahap 4 & 5 (WS-10 & WS-11) | **Penyelesaian WS-10 & WS-11:** Mengikuti panduan pengerjaan dari Dosen di kelas; eksekusi otomatisasi parameter `GridSearchCV` (C, Gamma, Kernel RBF); penguncian *random state* 42; pengisian checklist validasi data (*Data Validation Checklist*); serta penerimaan arahan struktur penyusunan Laporan Akhir. | [00-admin/README.md](README.md), [06-output/](../06-output/) |

## Status Ringkas

- **Tahap 1–4**: Selesai (dataset final: matrix 400 run / 40 replikasi per kombinasi, 2026-06-15).
- **Tahap 5**: Konten naskah selesai dengan statistik n=40 (termasuk tinjauan pustaka & verifikasi CVE-2026-48524); menyisakan keputusan bahasa final dan pemindahan ke template jurnal tujuan (dilakukan oleh peneliti).

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Lengkapi matriks literatur dengan paper *related work* nyata ([02-literatur/matriks-literatur.md](../02-literatur/matriks-literatur.md)) — 18 referensi terverifikasi
- [x] Verifikasi CVE-2026-48524 terhadap basis data NVD/MITRE — terkonfirmasi via GHSA-fhv5-28vv-h8m8 (PyJWT, CVSS 3.7)
- [ ] Tetapkan bahasa final naskah (Indonesia/Inggris) sesuai jurnal tujuan
- [ ] Pindahkan konten [07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md)/`.docx` ke template jurnal tujuan
- [ ] Finalisasi penempatan figure/tabel sesuai gaya jurnal
- [ ] Review akhir seluruh klaim numerik agar konsisten antar dokumen (lihat daftar pada [07-manuskrip/00-outline.md](../07-manuskrip/00-outline.md))

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
