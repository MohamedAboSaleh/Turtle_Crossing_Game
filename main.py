import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
index = 0

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    index += 1
    time.sleep(0.1)
    screen.update()
    if index % 6 == 0:
        car_manager.add_car()
    car_manager.move_cars()

    # player crossed finish line
    if player.crossed_finish_line():
        car_manager.increase_speed()
        player.reset()
        scoreboard.increase_level()

    # detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
