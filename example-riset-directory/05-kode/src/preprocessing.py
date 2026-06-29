from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

# Inisialisasi stemmer di LUAR fungsi agar hanya dibuat sekali
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def clean_text(text):
    # Membersihkan teks
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Stemming menggunakan objek yang sudah dibuat di atas
    return stemmer.stem(text)

if __name__ == "__main__":
    # Tes sistem
    contoh = "Selamat datang! Anda menang hadiah 1 Miliar, klik link ini."
    print(f"Hasil sistem: {clean_text(contoh)}")

    import matplotlib.pyplot as plt

