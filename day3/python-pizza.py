# find cost of pizza depending on the size, if user wants pepperoni, and if user wants extra cheese.
cost = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    cost += 15
elif size == "M":
    cost += 20
elif size == "L":
    cost += 25
else:
    print("Something went wrong")

if add_pepperoni == "Y" and size == "S":
    cost += 2
else:
    cost += 3

if extra_cheese == "Y":
    cost += 1

print(f"Your final bill is: ${cost}.")
