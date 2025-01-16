import pandas as pd

df = pd.read_csv("C:/Users/Ebubekir13/Desktop/Ders/Makine Öğrenmesi/IRIS.csv")

#(unique) türleri ve her bir türün sayısını ekrana yazdır
species_counts = df['species'].value_counts()
print("Her bir türün sayısı:")
for species, count in species_counts.items():
    print(f"{species}: {count}")

# One-hot encoding işlemi için hazırlık
unique_species = df['species'].unique()
print("\nBenzersiz türler:", unique_species)

# One-hot encoding işlemi
encoded_data = []
for _, row in df.iterrows():
    # Her bir tür için bir satır oluştur
    encoded_row = list(row[:-1])  # 'species' sütunundan önceki özellik sütunlarını al
    for species in unique_species:
        # İç içe döngü ile one-hot encoding: Mevcut tür ile eşleşiyorsa 1, değilse 0 koy
        encoded_row.append(1 if row['species'] == species else 0)
    encoded_data.append(encoded_row)

# Yeni sütun isimlerini belirleme kısmı
feature_columns = df.columns[:-1]  # 'species' sütunundan önceki özellik sütunları
encoded_columns = feature_columns.tolist() + [f"species_{s}" for s in unique_species]
df_encoded = pd.DataFrame(encoded_data, columns=encoded_columns)

# One-hot encoding sonrası veri çerçevesini ekrana yazdırma
print("\nOne-hot encoding sonrası veri çerçevesi:")
print(df_encoded)

# Geliştirilmiş haliyle One-hot encoding sonrası her bir türe göre sütunları yazdırma işlemi
print("\nOne-hot encoding sonrası sütun isimleri:")
print(df_encoded.columns.tolist())

# One-hot encoded veri çerçevesini Excel dosyası olarak kaydetme kısmı
output_file = "C:/Users/Ebubekir13/Desktop/Ders/Makine Öğrenmesi/IRIS_encoded.xlsx"
df_encoded.to_excel(output_file, index=False)
print(f"\nOne-hot encoded veri çerçevesi '{output_file}' dosyasına kaydedildi.")
