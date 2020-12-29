from turtle import Turtle
import turtle
START_POINT = (0, -270)
MOVE_DISTANCE = 20
FINISH_LINE = 290


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.seth(90)
        self.goto(START_POINT)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def reset(self):
        self.goto(START_POINT)


    def at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False