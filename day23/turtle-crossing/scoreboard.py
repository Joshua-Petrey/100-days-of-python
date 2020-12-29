from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.color('white')
        self.write(f"Level: {self.level}", align='left',
                   font=('Arial', 18, 'normal'))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='left',
                   font=('Arial', 18, 'normal'))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=('Arial', 18, 'normal'))
