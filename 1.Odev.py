import numpy as np

# 3x3 Karışıklık Matrisi (Mavi, Yeşil, Kırmızı)
confusion_matrix_3x3 = np.array([
    [30, 5, 2],  # Gerçek Mavi
    [6, 40, 4],  # Gerçek Yeşil
    [3, 7, 35]   # Gerçek Kırmızı
])

# Metrik hesaplama fonksiyonu
def calculate_metrics(confusion_matrix):
    metrics = {}
    total_samples = confusion_matrix.sum()  # Toplam örnek sayısı
    for i in range(3):  # 3 sınıf için döngü
        TP = confusion_matrix[i, i]  # Doğru Pozitif (True Positive) sayısı
        FP = confusion_matrix[:, i].sum() - TP  # Yanlış Pozitif (False Positive)
        FN = confusion_matrix[i, :].sum() - TP  # Yanlış Negatif (False Negative)
        TN = total_samples - (TP + FP + FN)  # Doğru Negatif (True Negative)

        # Doğruluk (Accuracy)
        accuracy = (TP + TN) / total_samples if total_samples > 0 else 0

        # Hassasiyet (Precision)
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0

        # Duyarlılık (Recall veya TPR)
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0

        # Özgünlük (Specificity)
        specificity = TN / (TN + FP) if (TN + FP) > 0 else 0

        # F1 Skor
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        # Her sınıf için metrikleri kaydet
        metrics[f"Sınıf {i+1}"] = {
            "Doğruluk (Accuracy)": accuracy,
            "Hassasiyet (Precision)": precision,
            "Duyarlılık (Recall)": recall,
            "Özgünlük (Specificity)": specificity,
            "F1 Skor": f1_score
        }

    return metrics

# Hesaplamaları yap ve çıktıları göster
metrics = calculate_metrics(confusion_matrix_3x3)
for sınıf, değerler in metrics.items():
    print(f"{sınıf} Metrikleri:")
    for metrik, değer in değerler.items():
        print(f"  {metrik}: {değer:.2f}")
    print()
