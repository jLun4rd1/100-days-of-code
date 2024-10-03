from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color:')

colors = ['red','orange','yellow','green','blue','purple']

x = -230
y = -100

all_turtles = []

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    all_turtles.append(turtle)
    y += 40
    
if user_bet:
    is_race_on = True
    
while is_race_on == True:
    for turtle in all_turtles:        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        
        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
            
            is_race_on = False

screen.exitonclick()