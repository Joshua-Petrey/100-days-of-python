def turn_right():
    turn_left()
    turn_left()
    turn_left()

# find a wall then turn left to get a wall on the right
while front_is_clear():
	move()
turn_left()

# will not be infinite as long as there is a wall on the right
while not at_goal():
	if right_is_clear():
		turn_right()
		move()
	elif front_is_clear():
		move()
	else:
		turn_left()