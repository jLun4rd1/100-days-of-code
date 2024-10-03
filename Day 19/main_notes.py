# Event Listeners
from turtle import Turtle, Screen

my_turtle = Turtle() # <<< an instance
screen = Screen()

my_turtle.color('green') # <<< green state

# Listen to keyboard inputs
screen.listen()

print(my_turtle.position())

screen.exitonclick()