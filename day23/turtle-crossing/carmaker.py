from turtle import Turtle
import random
colors = ['red', 'blue', 'green', 'orange', 'pink', 'azure', 'beige', 'tomato', 'firebrick']
X = 305
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarMaker():

    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def go_left(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def generate_cars(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 6: 
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.goto(X, random.randint(-250, 280))
            self.all_cars.append(new_car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT