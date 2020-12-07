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
part1 = input()
print(r.choice(questions))
part2 = input()
print("Your band name could be" + "\n" + part1 + " " + part2)
