from turtle import Screen, Turtle, speed
import random

leo = Turtle()
screen = Screen()
screen.colormode(255)
leo.speed('fastest')

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

def draw_spirograph(size, num_circles):
	for _ in range(num_circles):
		leo.circle(size)
		leo.left(360 / num_circles)
		leo.pencolor(random_color())

draw_spirograph(150, 50)

screen.exitonclick()