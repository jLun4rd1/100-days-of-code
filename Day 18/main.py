# import colorgram
import turtle as t
import random

screen = t.Screen()
screen.screensize(500,500)

t.colormode(255)

my_turtle = t.Turtle()
my_turtle.hideturtle()
my_turtle.speed(10)

# raw_colors = colorgram.extract('test.jpeg', 40)

# def get_color_list(color_image):
#     color_code_list = []
#     for color in color_image:
#         r = color.rgb[0]
#         g = color.rgb[1]
#         b = color.rgb[2]
#         color_code = (r,g,b)
#         color_code_list.append(color_code)
#     return color_code_list    

# color_code_list = get_color_list(color_image=raw_colors)

color_list = [
            (1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), 
            (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), 
            (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), 
            (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135),
            (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209),
            (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45),
            (61, 65, 66)
]

my_turtle.setheading(225)
my_turtle.penup()
my_turtle.forward(300)

start_position = my_turtle.position()

x = start_position[0]
y = start_position[1]

spot_size = 20
space_in_between = 50

for i in range(10):
    for i in range(10):
        my_turtle.color(random.choice(color_list))
        my_turtle.teleport(x=x, y=y)
        my_turtle.dot(20)
        x += 50
    x = start_position[0]
    y += 50

screen.exitonclick()