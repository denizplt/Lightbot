# combined classes
from kernel import Kernel  # kernel class
from level_info import HeightInfo, LightInfo  # classes of level informations
from visualization import Visual  # visualization functions
import numpy as np

"örnek level oluşturuldu"
# creating level information 
position =[[2,5],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[4,4],[4,5],[4,6],[4,7],[4,8]] # heights' positions
number = [1,2,2,2,4,2,3,2,4,3,4,2,2] # height levels
lights = [(2, 3), (4, 5)]  # light positions

# creating height and light matrices
height_info = HeightInfo(position, number)
height_matrix = height_info.create_height_matrix()
print(height_matrix)
light_info = LightInfo(lights)
light_matrix = light_info.create_light_matrix()

print("Height Matrix:")
print(height_matrix)

print("\nLight Matrix:")
print(light_matrix)

# starting the kernel (load the bot and level)
kernel = Kernel(height_matrix=height_matrix, light_matrix=light_matrix, terrain=height_matrix)

# visualizing the chessboard and level
level1 = Visual(height_matrix)
level1.baseterrain()  # base terrain
level1.levelterrain()  # drawing height information

# getting commands from the user and process them

while True:
    user_input = input("Enter a command (type 'q' to quit): ")
    if user_input == "q":
        print("Exiting loop...")
        break
    else:
        print(f"You entered: {user_input}")
        
        
        
"İlerleyen ödevlerle birlikte visualization classına komut tuşları eklenecektir."
