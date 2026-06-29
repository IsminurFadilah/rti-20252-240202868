import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from preprocessing import clean_text 

# 1. Load data asli dari folder 04-data
# Pastikan nama kolomnya benar (misal: 'text' untuk isi sms, 'label' untuk 0 atau 1)
df = pd.read_csv('04-data/dataset-sms-spam.csv')

# 2. Preprocessing (Membersihkan teks)
print("Sedang membersihkan teks...")
# Baris tambahan ini memastikan data kosong diisi dengan string kosong agar tidak error
df['Teks'] = df['Teks'].fillna('') 
df['cleaned'] = df['Teks'].apply(clean_text)

# 3. Vektorisasi
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned'])
y = df['label']

# 4. Latih Model SVM
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# 5. Evaluasi
predictions = model.predict(X_test)
print("Hasil Klasifikasi dengan Data Asli:")
print(classification_report(y_test, predictions))