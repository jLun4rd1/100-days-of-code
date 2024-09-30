import turtle as t
import random as r

screen = t.Screen()
my_turtle = t.Turtle()

my_turtle.shape("turtle")
my_turtle.color("red")

my_turtle.width(10)
my_turtle.speed(10)

color_pallette = ['red', 'tomato', 'purple', 'medium purple', 'yellow', 'gold', 'green', 'lime green']

angles = [0, 90, 180, 270]

for i in range(250):
    my_turtle.color(r.choice(color_pallette))
    my_turtle.forward(20)
    my_turtle.setheading(r.choice(angles))

screen.exitonclick()