from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight=600, canvwidth=800)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(x_y=(-350, 0))
r_paddle = Paddle(x_y=(350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 385 or ball.ycor() < -385:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if ball.x_move > 0:
            ball.x_move += 5
        else:
            ball.x_move -= 5
            
        if ball.y_move > 0:
            ball.y_move += 5
        else:
            ball.y_move -= 5

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        
screen.exitonclick()