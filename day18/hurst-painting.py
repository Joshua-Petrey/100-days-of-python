import colorgram
import random
from turtle import Screen, Turtle

leo = Turtle()
leo.speed('fastest')
leo.penup()
leo.hideturtle()
screen = Screen()
screen.colormode(255)

# colors = colorgram.extract('spots.jpg', 10)
# pallete = []
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	pallete.append((r,g,b))


paints = [(202, 164, 109), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21)]

num_dots = 101

def make_hurst():
	x = -460
	y = -360
	leo.setposition(x,y)
	for i in range(1, num_dots):
		leo.dot(20, random.choice(paints))
		leo.fd(50)
		if i % 10 == 0:
			y += 50
			leo.setposition(x, y)
			
make_hurst()
	
	
screen.exitonclick()