import random as r

rockart = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paperart = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissorsart = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(
    input("Rock, paper, or scissors, 0 for rock, 1 for paper, 2 for scissors.\n"))
computer = r.randint(0,2)

if player > 2:
	print("Only numbers 0, 1, or 2")
else:
	if player == 0:
		print(rockart)
		if computer == 0:
			print(f"Computer chose:{rockart}\n It's a draw!")
		elif computer == 1:	
			print(f"Computer chose:{paperart}\nYou lose")
		else:
			print(f"Computer chose:{scissorsart}\n You win!!!!!")

	if player == 1:
		print(paperart)
		if computer == 1:
			print(f"Computer chose:{paperart}\n It's a draw! ")
			print("It's a draw!")
		elif computer == 2:	
			print(f"Computer chose:{scissorsart}\n You lose")
		else:
			print(f"Computer chose:{rockart}\n You win!!!!!")
		
	if player == 2:
		print(scissorsart)
		if computer == 2:
			print(f"Computer chose:{scissorsart}\n It's a draw!")
		elif computer == 1:	
			print(f"Computer chose:{paperart}\n You Win!!!!")
			print("You Win!!!!")
		else:
			print(f"Computer chose:{rockart}\n You Lose")