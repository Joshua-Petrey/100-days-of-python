from turtle import Turtle
from random import randint, random

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.75, stretch_wid=0.75)
		self.color('yellow')
		self.speed('fastest')
		self.new_location()

	def new_location(self):	
		random_x = randint(-280, 280)
		random_y = randint(-280, 280)
		self.goto(random_x,random_y) # when created got random position

