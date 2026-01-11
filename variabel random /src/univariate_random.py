import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("../dataset/dataset_univariate.csv")

# Statistik dasar
mean = data["nilai"].mean()
variance = data["nilai"].var()
std_dev = data["nilai"].std()

print("Mean:", mean)
print("Varians:", variance)
print("Standar Deviasi:", std_dev)

# Visualisasi
plt.hist(data["nilai"], bins=5)
plt.title("Histogram Variabel Random Univariat")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.show()
