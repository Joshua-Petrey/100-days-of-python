from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank = []
# take objects from question_data and turn them into instances of the Question class
# then append them to the question_bank list
for x in question_data:
	question_bank.append(Question(x.get('text'), x.get('answer')))

brain = Quiz_brain(question_bank)

while brain.has_questions_left(question_bank):
	brain.next_question()

print('You completed the quiz')
print(f'Your final score was {brain.score}/{brain.question_number}')