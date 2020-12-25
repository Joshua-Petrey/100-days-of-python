from turtle import Screen, Turtle, color, forward, onkeypress, shape
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    "Choose a color", "Which turtle will win the race?")
is_race_on = False
colors = ['blue', 'red', 'orange', 'pink', 'green', 'purple']
y_positions = [-100, -50, -20, 20, 50, 100]
all_turtles = []


# create 6 new turtles with different colors and positions
for turtle in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)


# if use_bet exists
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win! The winner was the {user_bet} turtle")
            else:
                print(f"You Lost! The winner was the {winner} turtle")
        rand_speed = random.randint(0, 10)
        turtle.forward(rand_speed)


screen.exitonclick()
