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

## ## Item Tindak Lanjut (Checklist Progres Riset)

- [x] Konfirmasi validitas dataset sekunder bahasa Indonesia (1.623 baris data teks dari repositori Yudi Wibisono)
- [x] Penyusunan draf proposal penelitian di dalam repositori (`01-proposal/proposal-penelitian.md`)
- [x] Pemetaan studi literatur dan analisis gap terhadap 4 paper acuan utama (`02-literatur/matriks-literatur.md`)
- [x] Desain arsitektur alur komputasi data (*Machine Learning Pipeline* dengan diagram Mermaid di `03-teori/arsitektur-dan-skema.md`)
- [x] Penentuan bahasa naskah final menggunakan standar Bahasa Indonesia untuk laporan Universitas Putra Bangsa
- [x] Sinkronisasi dan pembersihan seluruh link antar-folder dari materi JWKS lama di VS Code
- [ ] Implementasi script pemrograman untuk *Text Preprocessing* (Sastrawi) dan ekstraksi fitur (TF-IDF Vectorizer) di folder `05-kode`
- [ ] Eksekusi pelatihan paralel model *Baseline* (Naïve Bayes) vs model Intervensi Utama (SVM + GridSearchCV)
- [ ] Evaluasi pengujian menggunakan *Confusion Matrix* untuk pembuktian target akurasi model SVM di atas 95%
- [ ] Pemindahan grafik visualisasi performa dan draf teks akhir dari Markdown ke dalam template laporan utama (.docx)

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
