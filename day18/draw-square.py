from turtle import Screen, Turtle

leo = Turtle()
leo.shape("circle")
leo.pencolor('black')

for _ in range(4):
	leo.fd(100)
	leo.left(90)





screen = Screen()
screen.exitonclick()