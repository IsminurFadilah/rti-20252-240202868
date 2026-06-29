import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from preprocessing import clean_text

# 1. Load Data
df = pd.read_csv('04-data/dataset-sms-spam.csv')

# Ambil data (hapus .head(500) jika ingin menggunakan seluruh data)
df = df.head(500) 

# Bersihkan Data (Hapus duplikasi pembersihan)
df['Teks'] = df['Teks'].fillna('')
df = df.dropna(subset=['label'])

# 2. Preprocessing
print("Sedang membersihkan teks... (harap tunggu)")
df['cleaned'] = df['Teks'].apply(clean_text)

# 3. Vektorisasi
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned'])
y = df['label']

# 4. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 5. Latih & Uji SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print("\n--- HASIL SVM ---")
print(classification_report(y_test, y_pred_svm))

# 6. Latih & Uji Naive Bayes
nb = MultinomialNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
acc_nb = accuracy_score(y_test, y_pred_nb)
print("\n--- HASIL NAIVE BAYES ---")
print(classification_report(y_test, y_pred_nb))

# 7. Visualisasi Grafik Otomatis
if not os.path.exists('06-output'):
    os.makedirs('06-output')

models = ['SVM', 'Naive Bayes']
accuracies = [round(acc_svm, 2), round(acc_nb, 2)]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracies, color=['#3498db', '#2ecc71'])
plt.ylim(0, 1.1)
plt.title('Perbandingan Akurasi Model')
plt.ylabel('Akurasi')
for i, v in enumerate(accuracies):
    plt.text(i, v + 0.01, str(v), ha='center', fontweight='bold')

plt.savefig('06-output/perbandingan_model.png')
print(f"\nGrafik disimpan di: 06-output/perbandingan_model.png")
plt.show()
