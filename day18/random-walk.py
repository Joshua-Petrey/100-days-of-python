from turtle import Screen, Turtle
import random

leo = Turtle()
leo.speed(10)
leo.shape("circle")
leo.pensize(10)
screen = Screen()
screen.colormode(255)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

directions = [0,90,180,270]

for _ in range(200):
	leo.setheading(random.choice(directions))
	leo.fd(25)
	leo.pencolor(random_color())

screen.exitonclick()