from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y
        self.move_distance = MOVE_DISTANCE
        
    def move_up(self):
        self.forward(self.move_distance)
        
    def reset(self):
        self.goto(STARTING_POSITION)