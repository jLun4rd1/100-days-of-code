# WHAT I DID!!
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.x_pos = 320
        self.y_pos = random.randint(-180, 180)
        self.goto(self.x_pos, self.y_pos)
        self.move_distance = STARTING_MOVE_DISTANCE
        
    
    def move(self):
        self.x_pos -= self.move_distance
        self.goto(self.x_pos, self.y_pos)
