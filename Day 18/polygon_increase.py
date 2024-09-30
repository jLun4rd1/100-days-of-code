import turtle as t
import random as r

screen = t.Screen()
my_turtle = t.Turtle()

my_turtle.shape("turtle")
my_turtle.color("dim gray")

screen.colormode(255)

def draw_shape(num_sides):
    angle = 360/num_sides 
    for i in range(0,num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)
    num_sides += 1
    
    return num_sides

sides = 3

while sides <= 10:
    tup = (r.randint(50,255), r.randint(1,255), r.randint(1,255))
    my_turtle.color(tup)
    sides = draw_shape(num_sides=sides)

screen.exitonclick()