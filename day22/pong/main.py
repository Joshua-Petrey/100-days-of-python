from scoreboard import Scoreboard
import turtle
from ball import Ball
from turtle import Screen, Turtle, xcor
from paddle import PADDLE_1_START, PADDLE_2_START, Paddle
from time import sleep
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.listen()
screen.tracer(0)

# draw paddles, ball, scoreboard
pad_1 = Paddle(PADDLE_1_START)
pad_2 = Paddle(PADDLE_2_START)
scoreboard = Scoreboard()
ball = Ball()

#
screen.onkey(pad_1.up, "w")
screen.onkey(pad_1.down, "s")
screen.onkey(pad_2.up, "Up")
screen.onkey(pad_2.down, "Down")


game_on = True
while game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

# top and bottom ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# ball + paddle collision detection
    if ball.distance(pad_2) < 50 and ball.xcor() > 330 or ball.distance(pad_1) < 50 and ball.xcor() < -330:
        ball.bounce_x()

# ball offscreen add point to other player, update score
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.p1_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.p2_point()


screen.exitonclick()
