# Generate a band name from the answers of two randomly chosen questions
import random as r
questions = ("What is your pet\'s name?",
             "What is your nickname?",
             "What is your favorite color?",
             "What is your favorite planet",
             "What is your favorite word?",
             "What is your favorite dance?",
             "What is your last name?",
             "What your favorite smell?",
             "What is your favorite food?",
             )

print(r.choice(questions))
answer1 = input().capitalize()
print(r.choice(questions))
answer2 = input().capitalize()
print("Your band name could be" + "\n" + answer1 + " " + answer2)
