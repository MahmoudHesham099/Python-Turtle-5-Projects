from turtle import Screen
import time

from Car import Car
from Player import Player
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carObj = Car(screen)
player = Player(screen)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    # create and move cars
    carObj.create_car()
    carObj.move_cars()

    # car collision
    for car in carObj.all_cars:
        if car.distance(player) < 27:
            game_on = False
            scoreboard.game_over()

    # finish line
    if player.reach_finish_line():
        player.goto_start()
        carObj.level_up()
        scoreboard.level_up()

screen.exitonclick()