from random import random
from art import logo
import random

def play():

	def choose_difficulty():
		difficulty = input(f"Choose a difficulty: easy or hard\n")
		if difficulty == 'easy':
			attempts = 10
			return attempts 
		else:
			attempts = 5
			return attempts

	def logic():
		the_number = random.randint(1, 100)
		attempts_remaining = choose_difficulty()
		while attempts_remaining > 0:
			guess = int(input(f"Guess a number\n"))
			if guess > the_number:
				print("Guess was higher the the number")
				attempts_remaining -= 1
			elif guess < the_number:
				print("Guess was lower than the number")
				attempts_remaining -= 1
			elif guess == the_number:
				print(f"Correct, the number was {the_number}. You win!!!")
				break
		if attempts_remaining == 0:
			print(f"Sorry, you ran out of lives: Game Over. The number was {the_number}")

	print(logo)
	print("Welcome to the Guessing Game 😃\nI'm thinking of a number between 1 and 100.")
	logic()

play()
while input("Would you like to play again, y or n\n") == 'y':
	play()
