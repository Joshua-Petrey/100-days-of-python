def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    repeat 2:
        turn_right()
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
		move()