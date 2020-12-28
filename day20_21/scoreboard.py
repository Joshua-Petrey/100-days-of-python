from turtle import Turtle, hideturtle, pendown

ALIGN = 'center'
FONT = ("Arial", 16, 'normal')


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.show_score()
		self.hideturtle()

	def show_score(self):
		self.color('white')
		self.penup()
		self.goto(0, 275)
		pendown()
		#write the initial score of 0
		self.write(f"Score: {self.score}", move=False, align='center', font=("Arial", 16, 'normal'))

	def update_score(self):
		# have to erase the old score before writing the new score
		self.clear()
		self.score += 1
		self.write(f"Score: {self.score}", move=False, align='center', font=("Arial", 16, 'normal'))

	def game_over(self):
		self.home()
		self.write(f"GAME OVER", move=False, align='center', font=("Arial", 16, 'normal'))
