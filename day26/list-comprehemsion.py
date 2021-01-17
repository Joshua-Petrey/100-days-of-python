numbers = [1, 2, 3, 4, 5, 6, 7]
[print(x**2) for x in numbers]

# create an array of squared numbers
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

# create an array if the index value is > 20
greater_than_20 = [number for number in squared_numbers if number > 20]
print(greater_than_20)

# plus 1
plus_one = [number + 1 for number in numbers]
print(plus_one)

# list comprehensions work on strings
name = "Joshua"
letters_in_name = [letter for letter in name]
print(letters_in_name)

# H,o,s,h,u,a   If letter is != J return letter else return "H" if letter is J
newlist = [letter if letter != "J" else "H" for letter in name]
print(newlist)

# 1,2,3,4
rangelist = [num for num in range(1, 5)]
print(rangelist)
