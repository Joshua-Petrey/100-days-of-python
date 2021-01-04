print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
split = int(input("How many people are splitting the bill? "))
answer = round((total + (total * (tip / 100))) / split, 2)
# format to show both cents places
formatted_answer = "{:.2f}".format(answer)
print(formatted_answer)
