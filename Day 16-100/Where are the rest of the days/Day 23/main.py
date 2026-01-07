import random
import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move, "w")
sleep_time = 0.1

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)

    if random.randint(1, 6) == 1:
        car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 220:
        scoreboard.update_level()
        player.reset_position()
        sleep_time *= 0.8
        time.sleep(sleep_time)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            sleep_time = 0.1
            time.sleep(sleep_time)
            player.reset_position()
            scoreboard.reset_level()

    screen.update()