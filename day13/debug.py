###########DEBUGGING#####################
# # Describe Problem
# 20 is not inclusive, change to 21
from random import randint


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# # Reproduce the Bug
# zero will not be selected,change 1 to 0
# 6 will cause a index error, change 6 to 5
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
# can't choose year 1994, set one of the 1994's to be inclusive
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

  # Fix the Errors
  # input needs to be converted to int, and conditional should be => 18
  # print needs an f to use format variables
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

  # Print is Your Friend
  # words_per_page is set to compare not assign
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Use a Debugger
# The append needs to happen inside the for loop


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    	b_list.append(new_item)
    print(b_list)


