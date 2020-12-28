from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('segments')
screen.tracer(0)  # turn off tracer

#snake, food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
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

    # check for head and food collision, update the score
    if snake.head.distance(food) < 15:
        food.new_location()
        scoreboard.update_score()
        snake.grow()
    # check for wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        scoreboard.game_over()
        game_on = False

    # tail collision detection
    for part in snake.segments[1:]:
        if snake.head.distance(part) < 10:
            game_on = False
            scoreboard.game_over() 

screen.exitonclick()
