import turtle
import pandas as pd

states_data = pd.read_csv('./50_states.csv')

#screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# turtle setup
artist = turtle.Turtle()
artist.hideturtle()
artist.penup()

all_states = states_data.state.to_list()
states_guessed = []


while len(states_guessed) < 50:

    user_input = screen.textinput(title=f"Correct: {len(states_guessed)}/50 ", prompt="What's the state's name?").title()

    if user_input == "Exit":
        missed_states = [state for state in all_states if state not in states_guessed]
        #create DFrame from missed_states list
        new_data = pd.DataFrame(missed_states)
        # create csv from the dataframe
        new_data.to_csv('./missed_states.csv')
        break
    elif user_input not in all_states or user_input in states_guessed:
        pass
    elif user_input in all_states and user_input not in states_guessed:
        states_guessed.append(user_input)
        # get row data of guessed state
        state_data = states_data[states_data.state == user_input]
        artist.goto(int(state_data.x), int(state_data.y))
        artist.write(f"{user_input}", font=("Arial", 12, "normal"))
        