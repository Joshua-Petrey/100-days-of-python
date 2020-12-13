def log(fun):
	return print(fun)

def sum(x,y):
	return x + y

log(sum(6, 10))


zero = 0
switch = True
while switch is True:
	zero += 1
	print(zero)
	if zero == 10:
		switch = False


# not flips condition

def turn_right():
    repeat 3:
        turn_left()

def hurdle():
    move()
    turn_left()
    move()
    repeat 2:
        turn_right()
        move()
    turn_left()
#while not at_goal
#while at_goal != True
while not at_goal():
    hurdle()



