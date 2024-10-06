from turtle import Turtle
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-225, 250)
        self.level = 1
    
    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)
        
    def increase_level(self):
        self.level += 1   
        self.write_level()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)