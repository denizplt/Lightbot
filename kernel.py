
# class of kernel of the game  
class Kernel: 
    # Initialises the start position and orientation, height map and terrain matrix. 
    def __init__(self, bot_x=0, bot_y=0, bot_z=0, bot_direction="right", height_matrix=None, light_matrix=None, terrain=None):
        self.bot_x = bot_x
        self.bot_y = bot_y
        self.bot_z = bot_z
        self.bot_direction = bot_direction
        self.height_matrix = height_matrix 
        self.light_matrix = light_matrix 
        self.terrain = terrain if terrain is not None else [[0 for _ in range(10)] for _ in range(10)]
        # This function gets information from classes in other files.
        

    # printing the current state of the bot (position and direction)
    def print_status(self):
        print(f"Bot position: ({self.bot_x}, {self.bot_y}, {self.bot_z}), Facing: {self.bot_direction}")
        for row in self.terrain:
            print(" ".join(str(cell) for cell in row)) # printing the land matrix
        print("\n")


    # Switches on the light at the bot's location (makes 1).
    def switch_light(self):
        self.terrain[self.bot_y][self.bot_x] = 1
        

    # Moves the bot one step forward according to its current direction, controls the boundaries.
    def move_forward(self):
        if self.bot_direction == "up" and self.bot_y > 0:
            self.bot_y -= 1
        elif self.bot_direction == "down" and self.bot_y < 9:
            self.bot_y += 1
        elif self.bot_direction == "right" and self.bot_x < 9:
            self.bot_x += 1
        elif self.bot_direction == "left" and self.bot_x > 0:
            self.bot_x -= 1


    # Rotates the bot to the left (updates its orientation).
    def turn_left(self):
        """Turn the bot left."""
        if self.bot_direction == "right":
            self.bot_direction = "up"
        elif self.bot_direction == "up":
            self.bot_direction = "left"
        elif self.bot_direction == "left":
            self.bot_direction = "down"
        elif self.bot_direction == "down":
            self.bot_direction = "right"
            
            
    # Rotates the bot to the right (updates its orientation).
    def turn_right(self):
        """Turn the bot right."""
        if self.bot_direction == "right":
            self.bot_direction = "down"
        elif self.bot_direction == "down":
            self.bot_direction = "left"
        elif self.bot_direction == "left":
            self.bot_direction = "up"
        elif self.bot_direction == "up":
            self.bot_direction = "right"
       
    
    # Jumps the bot according to the height map (to a new z-position).        
    def jump(self):
        """Jump to the next level if possible (based on height map)."""
        if self.bot_z < self.height_map[self.bot_y][self.bot_x]:
            self.bot_z = self.height_map[self.bot_y][self.bot_x]
        else:
            print("Jump not possible, no height difference.")


    # processes the given commands and directs the bot
    def process_commands(self, commands):
        for command in commands:
            if command == "^": 
                self.move_forward() # forward movement
            elif command == ">":
                self.turn_right() # right turn
            elif command == "<":
                self.turn_left() # left turn
            elif command == "@":
                self.switch_light() # light switch on 
            elif command =="J":
                self.jump() # jumping
            self.print_status()


#example of usage 
#kernel = Kernel()
#commands = "^^>^<^@"
#kernel.process_commands(commands)