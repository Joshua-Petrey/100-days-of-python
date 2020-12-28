from turtle import Turtle, onkeypress
PADDLE_1_START = (-360, 0)
PADDLE_2_START = (360, 0)
KEYBOARD = 'keyboard'
ARROWS = 'arrows'


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.make_paddle(start_position)

    def make_paddle(self, start):
        self.penup()
        self.speed('fastest')
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(start)

    # controls
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
