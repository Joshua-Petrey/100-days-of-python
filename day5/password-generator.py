import random
print("Welcome to the Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_count = int(input("How many letters do you want in your password?\n"))
symbol_count = int(
    input("How many symbols do you want in your password?\n"))
number_count = int(input("How many numbers do you want in your password?\n"))

total_length = letter_count + symbol_count + number_count

temp = []
password = ""
for x in range(0, total_length + 1):
    if x < letter_count:
        temp.append(random.choice(letters))
    if x < symbol_count:
        temp.append(random.choice(symbols))
    if x < number_count:
        temp.append(random.choice(numbers))
		
# shuffle the order
random.shuffle(temp)

# put list items into string
for x in range(0, len(temp)):
    password += temp.pop()

print(password)
