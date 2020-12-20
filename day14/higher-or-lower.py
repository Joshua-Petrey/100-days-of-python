from art import logo, vs
from data import data
import random

print(logo)
score = 0
A = random.choice(data)
B = random.choice(data)
# Make sure B and A are not the same
while A == B:
	B = random.choice(data)

def compare_followers(A,B):
	if A['follower_count'] > B['follower_count']:
		return 'A'
	else: 
		return 'B'

def is_user_correct(guess):
	if guess == "A":
		return "A"
	else:
		return "B"

def show_options():
	print(f"Choice A: {A['name']}, a {A['description']} from the {A['country']} ")
	print(vs)
	print(f"Choice B: {B['name']}, a {B['description']} from the {B['country']} ")

print(logo)

should_continue = False
while not should_continue:
	show_options()
	print(f"Current score is {score}")
	guess = input("Who has the most followers? A or B\n")
	if compare_followers(A,B) == is_user_correct(guess):
		score += 1
		A = B
		B = random.choice(data)
		print(logo)
		print("Correct")
	else:
		print(f"Wrong! Game Over final score: {score}")
		should_continue = True

