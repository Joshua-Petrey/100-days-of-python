import random

print("Welcome to the coin tosser")
toss = random.randint(0,1)

if toss == 1:
	print("Landed on Heads")
else:
	print("Landed on Tails")