PLACE_HOLDER = "[name]"
names = []
# place all the names into names[]
with open('./Input/Names/invited_names.txt', 'r') as f:
    for _ in range(10):
        names.append(f.readline().strip())

# open template
with open("./Input/Letters/birthday_invite.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # strip new line from end of name
        stripped_name = name.strip()
        # create new letter with the new name attached
        new_letter = letter_contents.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



