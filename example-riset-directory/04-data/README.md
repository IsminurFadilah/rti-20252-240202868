# 04-data

Repositori dataset mentah dan data hasil pembersihan (*preprocessing*) — input utama untuk **Tahap 4 (Pemodelan)**.

## Isi Berkas (Dataset)

- **`sms_spam_raw.csv`** : Dataset asli berisi 1.623 baris teks SMS Bahasa Indonesia (berisi kolom: `text` dan `label`).
- **`sms_spam_cleaned.csv`** : Hasil *preprocessing* (Case Folding, Stopword Removal, Stemming Sastrawi) yang siap diolah menjadi vektor numerik.

## Metrik Metadata Data

- **Sumber Data:** Repositori Dataset SMS Spam Bahasa Indonesia (Yudi Wibisono).
- **Format:** Comma-Separated Values (CSV).
- **Struktur Label:** - `0` : SMS Normal (Ham)
    - `1` : SMS Spam (Iklan/Judi Online/Penipuan)

