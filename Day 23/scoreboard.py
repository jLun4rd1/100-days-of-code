from turtle import Turtle
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    
    def __init__(self, position=(-225, 250)):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.starting_position = position
        self.goto(self.starting_position)
    
    def write_level(self, game_level):
        self.clear()
        self.write(f"Level: {game_level}", align='center', font=FONT)
        
    def game_over(self):
        self.write(f"GAME OVER", align='center', font=FONT)