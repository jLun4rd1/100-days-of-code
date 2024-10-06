import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, 'Up')

car_list = []
car_creation_frequency = 6
frame_count = 0

game_level = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    scoreboard.write_level(game_level)
    
    # Determines how often a car is created based on car_creation_frequency and frame_count
    if frame_count % car_creation_frequency == 0:
        car = CarManager()
        # Increments car speed based on game_level
        car.move_distance += (game_level - 1) * MOVE_INCREMENT
        car_list.append(car)
    
    for car in car_list:
        car.move()
        
    frame_count += 1
    
    # Detects if the player reached the finish_line
    if player.ycor() >= player.finish_line:
        player.reset()
        game_level += 1
        # Makes car creation faster as player levels up
        if car_creation_frequency > 3:
            car_creation_frequency -= 1
        # Makes player movement faster every 3 levels
        if game_level % 3 == 0:
            player.move_distance += 5 
    
    # Detects if the player has hit a 
    for car in car_list:
        if player.distance(car) <= 23:
            end = Scoreboard(position=(0,0))
            end.game_over()
            game_is_on = False
    
screen.exitonclick()