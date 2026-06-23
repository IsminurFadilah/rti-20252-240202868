# Dokumentasi Arsitektur Alur Data dan Skema Komputasi ML

**Nama / NIM:** Ismi Nur Fadilah (240202868)  
**Judul Riset:** Analisis Komparatif Algoritma Support Vector Machine dan Naïve Bayes untuk Klasifikasi Teks SMS Spam Berbahasa Indonesia

---

## 1. Diagram Arsitektur Alur Komputasi (*Pipeline Machine Learning*)

Berikut adalah diagram alur data menggunakan modul **Mermaid** untuk menggambarkan bagaimana data teks mentah diproses selangkah demi selangkah hingga menghasilkan metrik evaluasi perbandingan:

graph TD
    A[Dataset Mentah: 1.623 SMS] --> B[Pipeline Preprocessing]
    
    subgraph Preprocessing Teks Sastrawi 1.0.1
        B --> B1[Case Folding: Huruf Kecil]
        B1 --> B2[Tokenizing: Buang Simbol/Angka]
        B2 --> B3[Stopword Removal: Buang Kata Umum]
        B3 --> B4[Stemming: Potong Imbuhan Kata]
    end
    
    B4 --> C[Ekstraksi Fitur: TF-IDF Vectorizer]
    C --> D{Pemisahan Data Rasio 80:20}
    
    D --> E1[80% Data Latih]
    D --> E2[20% Data Uji]
    
    subgraph Skenario Komparasi Pemodelan
        E1 --> F1[Skenario A: Multinomial Naive Bayes]
        E1 --> F2[Skenario B: SVM Kernel RBF + GridSearchCV]
    end
    
    F1 --> G1[Prediksi Label Model A]
    F2 --> G2[Prediksi Label Model B]
    
    G1 --> H1[Evaluasi Model A: Confusion Matrix]
    E2 --> H1
    
    G2 --> H2[Evaluasi Model B: Confusion Matrix]
    E2 --> H2
    
    H1 --> I[Matriks Perbandingan Performa Akhir]
    H2 --> I