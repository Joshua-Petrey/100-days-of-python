heights = input("Whare are the student heights?").split()

total = 0
items = 0
for height in heights:
	total += int(height)
	items += 1
print(round(total / items))