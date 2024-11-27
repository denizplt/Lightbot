
class Kernel:
    def __init__(self, bot_x=0, bot_y=0, bot_z=0, bot_direction="right", height_matrix=None, light_matrix=None, terrain=None):
        self.bot_x = bot_x
        self.bot_y = bot_y
        self.bot_z = bot_z
        self.bot_direction = bot_direction
        self.height_matrix = height_matrix 
        self.light_matrix = light_matrix 
        self.terrain = terrain if terrain is not None else [[0 for _ in range(10)] for _ in range(10)]
        
    def print_status(self):
        print(f"Bot position: ({self.bot_x}, {self.bot_y}, {self.bot_z}), Facing: {self.bot_direction}")
        for row in self.terrain:
            print(" ".join(str(cell) for cell in row))
        print("\n")



    def switch_light(self):
        self.terrain[self.bot_y][self.bot_x] = 1

    def move_forward(self):
        if self.bot_direction == "up" and self.bot_y > 0:
            self.bot_y -= 1
        elif self.bot_direction == "down" and self.bot_y < 9:
            self.bot_y += 1
        elif self.bot_direction == "right" and self.bot_x < 9:
            self.bot_x += 1
        elif self.bot_direction == "left" and self.bot_x > 0:
            self.bot_x -= 1

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
            
    def jump(self):
        """Jump to the next level if possible (based on height map)."""
        if self.bot_z < self.height_map[self.bot_y][self.bot_x]:
            self.bot_z = self.height_map[self.bot_y][self.bot_x]
        else:
            print("Jump not possible, no height difference.")


    def process_commands(self, commands):
        for command in commands:
            if command == "^":
                self.move_forward()
            elif command == ">":
                self.turn_right()
            elif command == "<":
                self.turn_left()
            elif command == "@":
                self.switch_light()
            elif command =="J":
                self.jump()
            self.print_status()


# Kullanım
#kernel = Kernel()
#commands = "^^>^<^@"
#kernel.process_commands(commands)
