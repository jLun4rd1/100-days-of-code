import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = (r, g, b)
    return color_code

def draw_spirograph(times, angle, radius):
    my_turtle.shape("turtle")
    my_turtle.speed(0)
    for i in range(times):
        my_turtle.setheading(angle)
        my_turtle.color(random_color())
        my_turtle.circle(radius)
        angle += 360/times

screen = t.Screen()
my_turtle = t.Turtle()

angle = 0
times = 7
radius = 50

draw_spirograph(times, angle, radius)

screen.exitonclick()