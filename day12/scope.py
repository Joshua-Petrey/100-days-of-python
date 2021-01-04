################### Scope ####################
enemies = 1

def increase_enemies():
  # python will use local variables
  # unless the global keyword is used to accesss the global variable
  # dont use global unless needed, document it
  global enemies
  enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Globals accessible anywhere, local variables accessible in functions only

# A function defined inside of another is only accessible inside outer function.
def game():
	def drink_potion():
		potion_strength = 2
		print(f"Health increased by {potion_strength}HP")
	drink_potion()

game()
# drink_potion() not accessible outside of game

# No block scope in python
# conditional blocks do not create a scope, 
# if enemies == 1:
	# if a variable was created here it would be accessible globally

# global keyword workaround
puppies = 1
def more_puppies():
	return puppies + 1

puppies = more_puppies()
print((puppies)) #2
puppies = more_puppies()
print((puppies)) #3


# global constants are global variables that will never be changed
# Naming convention is all uppercase with undescroes
PI = 3.1415
