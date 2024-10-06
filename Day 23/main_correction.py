import time
from turtle import Screen
from player_correction import Player
from car_manager_correction import CarManager
from scoreboard_correction import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    scoreboard.write_level()
    
    car_manager.create_cars()
    car_manager.move()
    
    # Detects colision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    # Detects finish line
    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_level()
            
screen.exitonclick()