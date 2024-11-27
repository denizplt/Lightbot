from kernel import Kernel  # Kernel sınıfı
from level_info import HeightInfo, LightInfo  # Level bilgileri
from visualization import Visual # Görselleştirme fonksiyonları
import numpy as np
# 1. Seviye bilgilerini oluştur
position =[[2,5],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[4,4],[4,5],[4,6],[4,7],[4,8]] # Yüksekliklerin pozisyonları
number = [1,2,2,2,4,2,3,2,4,3,4,2,2]# Yükseklik seviyeleri
lights = [(2, 3), (4, 5)]  # Işıkların pozisyonları

# Yükseklik ve ışık matrislerini oluştur
height_info = HeightInfo(position, number)
height_matrix = height_info.create_height_matrix()
print(height_matrix)
light_info = LightInfo(lights)
light_matrix = light_info.create_light_matrix()

print("Height Matrix:")
print(height_matrix)

print("\nLight Matrix:")
print(light_matrix)

# 2. Kernel'i başlat (botu ve seviyeyi yükle)
kernel = Kernel(height_matrix=height_matrix, light_matrix=light_matrix, terrain=height_matrix)

# 3. Satranç tahtasını ve seviyeyi görselleştir

level1 = Visual(height_matrix)
level1.baseterrain()  # Temel zemin
level1.levelterrain()  # Yükseklik bilgilerini çiz

# 4. Kullanıcıdan komutlar al ve işle
print("Komutlar: ^ = ileri, > = sağa dön, < = sola dön, @ = ışığı yak, J = zıpla, q = çıkış")


while True:
    user_input = input("Bir sayı girin (çıkmak için 'q'): ")
    if user_input == "q":
        print("Döngüden çıkılıyor...")
        break
    else:
        print(f"Girdiğiniz sayı: {user_input}")