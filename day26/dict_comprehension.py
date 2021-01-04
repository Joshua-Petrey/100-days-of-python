import random

# new dictionary from list
names = ['bob', 'james', 'barry']
# for each name in names, set the dict key to the current name and use a random number
# as it's value
new_dict = {student: random.randint(0,101) for student in names}
print(new_dict)

# get the students that passed with at least a score of 60
passed_students = {student: score for student, score in new_dict.items() if score >= 60}
print(passed_students)