from turtle import Screen, Turtle

leo = Turtle()
leo.shape("circle")
leo.pencolor('black')
leo.pensize(5)
for _ in range(20):
	leo.fd(10)
	leo.penup()
	leo.fd(10)
	leo.pendown()



screen = Screen()
screen.exitonclick()