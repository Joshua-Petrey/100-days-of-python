from turtle import Screen, Turtle
import turtle
import time
from snake import Snake
import scoreboard
import food


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('segments')
screen.tracer(0)  # turn off tracer

#snake
snake = Snake()
#listen for keyboard events
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()


game_on = True
while game_on:
    screen.update()  # update screen with new positions of all segments segments
    time.sleep(.1)  # add a delay between each update
    snake.move()

screen.exitonclick()
