from turtle import Screen, Turtle, onkeypress

leo = Turtle()
screen = Screen()
screen.listen()

def forwards():
	leo.fd(10)

def backwards():
	leo.back(10)

def turn_left():
	leo.left(5)

def turn_right():
	leo.right(5)
screen.listen()

def reset():
	leo.clear()
	leo.penup()
	leo.home()
	leo.pendown()

onkeypress(forwards, "Up")

onkeypress(backwards, "Down")

onkeypress(turn_left, "Left")

onkeypress(turn_right, "Right")

onkeypress(reset, "Delete")





screen.exitonclick()