#==============================|
#|----|----|----|----|----|----|
## >>>>>> Dashed line <<<<<<
# for i in range(0,10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
#|----|----|----|----|----|----|
#==============================|

#===================================|
#|----|----|----|----|----|----|----|
## >>>>>> IMPORT ONE MODULE <<<<<<
# from turtle import Turtle, Screen
## >>>>>> IMPORT EVERYTHING <<<<<<
# from turtle import *
#|----|----|----|----|----|----|----|
#===================================|

#======================================================================|
#|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
## >>>>>> INCREASING POLYGONS <<<<<<
# screen.colormode(255)

# def draw_shape(num_sides):
#     angle = 360/num_sides 
#     for i in range(0,num_sides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#     num_sides += 1
    
#     return num_sides

# sides = 3

# while sides <= 10:
#     tup = (r.randint(50,255), r.randint(1,255), r.randint(1,255))
#     my_turtle.color(tup)
#     sides = draw_shape(num_sides=sides)
#|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
#======================================================================|

#=========================================================================================================|
#|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
## >>>>>> RANDOM WALK <<<<<<
# my_turtle.width(10)
# my_turtle.speed(10)

# color_pallette = ['red', 'tomato', 'purple', 'medium purple', 'yellow', 'gold', 'green', 'lime green']

# angles = [0, 90, 180, 270]

# for i in range(250):
#     my_turtle.color(r.choice(color_pallette))
#     my_turtle.forward(20)
#     my_turtle.setheading(r.choice(angles))
#|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
#=========================================================================================================|

#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
## >>>>>> DRAW SPIROGRAPH <<<<<<
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_code = (r, g, b)
#     return color_code

# def draw_spirograph(times, angle, radius):
#     my_turtle.shape("turtle")
#     my_turtle.speed(0)
#     for i in range(times):
#         my_turtle.setheading(angle)
#         my_turtle.color(random_color())
#         my_turtle.circle(radius)
#         angle += 360/times

# screen = t.Screen()
# my_turtle = t.Turtle()

# angle = 0
# times = 45
# radius = 50

# draw_spirograph(times, angle, radius)
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

## IMPORT WITH ALIAS 
import turtle as t
import random

## TAPPING INTO THE MODULE
t.colormode(255)

screen = t.Screen()
my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

angle = 0
times = 45
radius = 50

screen.exitonclick()