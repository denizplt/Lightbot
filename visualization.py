from vpython import *
import numpy as np

# manual adjustment of the camera 
scene.camera.pos = vector(15,15,15)  # the position of the camera 
scene.camera.axis = vector(-10,-10,-10)  # the direction the camera is facing
scene.width = 800  # width (pixels)
scene.height = 600  # height (pixels)
scene.userzoom = False # switching off the zooming feature
scene.background = color.gray(0.5) #background colour


square_size = 1 # size of the square

# initial position of the terrain
start_x = 0 
start_z = 0 


# the class defined to visualise the terrain
"Şimdilik sadece terrain ve height verileri görselleştirildi, zamanla levelde görünecek olan lightların da visualizationı yapılacaktır."
class Visual:
  def __init__(self, height_matrix=None ):
    self.height_matrix = height_matrix
    
     
  def baseterrain(self):
    for row in range(10):  # 10 row
      for col in range(10):  # 10 column 
          # calculation of the position of squares
          x = start_x + col * square_size
          z = start_z + row * square_size

          # determination of colors of squares (black and white)
          color_value = color.white if (row + col) % 2 == 0 else vector(0, 0, 0)  # RGB (0, 0, 0) for black

          # creation of the square
          box(pos=vector(x, 0, z), size=vector(square_size, 0.1, square_size), color=color_value)


  # iteration over the height matrix to generate levels
  def levelterrain(self):
      for i in range(len(self.height_matrix)-1):
        for j in range(len(self.height_matrix)-1):
          if self.height_matrix[i,j] != 0: # checking whether the height at a given matrix position is non-zero 
            for k in range(int(self.height_matrix[i,j])): # for each non-zero height value, stack the boxes to form the terrain
              box(pos=vector(i, k, j), size=vector(square_size, square_size, square_size), color=color.blue) # creating a box in the correct position with the height corresponding to the matrix

   
        
        
        
