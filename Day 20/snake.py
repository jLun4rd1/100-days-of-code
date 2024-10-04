from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):    
        for position in STARTING_POSITIONS:
            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.penup()
            turtle.position = (position)
            self.turtles.append(turtle)
    
    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[index - 1].xcor()
            new_y = self.turtles[index - 1].ycor()
            self.turtles[index].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)    
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # if self.head.heading() == 0:
        #     self.head.left(90)
        # if self.head.heading() == 180:
        #     self.head.right(90)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # if self.head.heading() == 0:
        #     self.head.right(90)
        # if self.head.heading() == 180:
        #     self.head.left(90)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # if self.head.heading() == 90:
        #     self.head.left(90)
        # if self.head.heading() == 270:
        #     self.head.right(90)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # if self.head.heading() == 90:
        #     self.head.right(90)
        # if self.head.heading() == 270:
        #     self.head.left(90)