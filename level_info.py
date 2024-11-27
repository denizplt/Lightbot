# For every level, information about heights and lights are defined with matrices.
"Bu classların sonraki projelerde birleştirilmesi ve levellerin tek bir nesneyle oluşturulması planlanıyor. "

import numpy as np # Before necessary information is defined, zero matrices are created by using numpy library.

# Class for information about height
class HeightInfo:
    def __init__(self, position, number):
        self.position = position # Position of heights 
        self.number = number # Number of heights

    def create_height_matrix(self): 
        if len(self.position) != len(self.number): # Just in case lists of positions and numbers of heights are not equal.
            raise ValueError("Position and heights lists must have the same length.")

        height_matrix = np.zeros([10, 10])
        b = 0

        for i in self.position:
            if i[0] >= 10 or i[1] >= 10: # Elements of lists must not be out of matrix bounds. 
                raise ValueError(f"Position {i} is out of matrix bounds.")

            height_matrix[i[0], i[1]] = self.number[b] # Positions and number of heights are matched.
            b += 1

        return height_matrix
    

# Class for information about light 
class LightInfo:
    def __init__(self, light_positions):
        self.light_positions = light_positions # Position of lights
    
    def create_light_matrix(self):
        light_matrix = np.zeros((10, 10), dtype=int)
        for j in self.light_positions: # If there is a light on the position, 1 are written in the matrix to run in the kernel.
            light_matrix[j[0], j[1]] = 1 
        return light_matrix
    
# Examples for test (For every level, this information is updated.)
#positions = [(2, 3), (4, 5), (6, 7)]
#heights = [1, 2, 3]

#lights = [(2, 3), (4, 5)]

# Object of height information
#height_info = HeightInfo(positions, heights)
#height_matrix = height_info.create_height_matrix()

# Object of light information
#light_info = LightInfo(lights)
#light_matrix = light_info.create_light_matrix()

# Output is printed.
#print("Height Matrix:")
#print(height_matrix)

#print("\nLight Matrix:")
#print(light_matrix)