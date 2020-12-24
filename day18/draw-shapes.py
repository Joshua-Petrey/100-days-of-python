from turtle import Screen, Turtle, pencolor
import random
import turtle
leo = Turtle()
screen = Screen()
screen.colormode(255)


def random_color():
    leo.pencolor((random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)))


def shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        leo.fd(100)
        leo.left(angle)


for _ in range(3, 11):
    shape(_)
    random_color()

screen.exitonclick()
