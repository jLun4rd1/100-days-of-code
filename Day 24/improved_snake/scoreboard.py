from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = data.read()
        print('init', type(self.high_score))
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 14, "bold"))
    
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.high_score = open('data.txt', mode='r').read()
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()