import random

people = input("Type some names").split(", dave, mike")
payer = random.randint(0, len(people))

print(f"{people[payer]} is going to buy the meal today!")
