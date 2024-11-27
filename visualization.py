from vpython import *
import numpy as np
# Kamerayı manuel olarak ayarla
scene.camera.pos = vector(15,15,15)  # Kameranın pozisyonu
scene.camera.axis = vector(-10,-10,-10)  # Kameranın baktığı yön
scene.width = 800  # Genişlik (piksel)
scene.height = 600  # Yükseklik (piksel)

# Zoom'u devre dışı bırak
scene.userzoom = False

scene.background = color.gray(0.5)
# Kare boyutunu belirle
square_size = 1

# Satranç tahtasının başlangıç pozisyonu
start_x = 0 
start_z = 0 


class Visual:
  def __init__(self, height_matrix=None ):
    self.height_matrix = height_matrix
    
     
  def baseterrain(self):
    for row in range(10):  # 8 satır
      for col in range(10):  # 8 sütun
          # Karelerin pozisyonunu hesapla
          x = start_x + col * square_size
          z = start_z + row * square_size

          # Karelerin renklerini belirle (siyah-beyaz dönüşümlü)
          color_value = color.white if (row + col) % 2 == 0 else vector(0, 0, 0)  # Siyah için RGB (0, 0, 0)

          # Kareyi oluştur
          box(pos=vector(x, 0, z), size=vector(square_size, 0.1, square_size), color=color_value)



  def levelterrain(self):
      for i in range(len(self.height_matrix)-1):
        for j in range(len(self.height_matrix)-1):
          if self.height_matrix[i,j] != 0:
            for k in range(int(self.height_matrix[i,j])):
              box(pos=vector(i, k, j), size=vector(square_size, square_size, square_size), color=color.blue)

   
        
        
        
