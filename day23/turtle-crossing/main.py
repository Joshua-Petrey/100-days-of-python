from turtle import Screen, Turtle
from player import FINISH_LINE, Player
from carmaker import CarMaker, MOVE_INCREMENT, START_MOVE_DISTANCE
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# initialize
leo = Player()
level = Scoreboard()
cars = CarMaker()

# controls
screen.onkey(leo.up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_cars()
    cars.go_left()

    if leo.at_finish_line() == True:
        leo.reset()
        level.increase_level()
        cars.increase_car_speed()

    for car in cars.all_cars:
        if leo.distance(car) < 27:
            level.game_over()
            game_on = False

screen.exitonclick()
