import random
# make a list of names
people = input("Type some names").split(", ")
# grab random name
payer = random.randint(0, len(people))

print(f"{people[payer]} is going to buy the meal today!")
