from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

screen.listen()

print(my_turtle.position())

speed = 10

def move_forwards():
    my_turtle.forward(speed)
    
def move_backwards():
    my_turtle.backward(speed)
    
def turn_clockwise():
    my_turtle.right(15)
    
def turn_counter_clockwise():
    my_turtle.left(15)
    
def clear():
    global speed
    speed = 10
    screen.resetscreen()
    
def speed_up():
    global speed 
    speed += 10
    
def slow_down():
    global speed
    if speed > 0:
        speed -= 10

screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='c', fun=clear)
screen.onkey(key='e', fun=speed_up)
screen.onkey(key='q', fun=slow_down)

screen.exitonclick()