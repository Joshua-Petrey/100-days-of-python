class Quiz_brain:
	def __init__(self, question_list):
		self.question_number = 0
		self.question_list = question_list
		self.score = 0

	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		user_answer = input(f'Q.{self.question_number}: {current_question.text} True/False\n')
		# pass user's answr and the correct answer to chech_answer()
		self.check_answer(user_answer, current_question.answer)


	def has_questions_left(self, q_bank):
		if self.question_number < len(q_bank):
			return True
		else:
			 False

	def check_answer(self, user_answer, correct_answer):
		if user_answer.lower() == correct_answer.lower():
			print(f"Correct, The answers was {correct_answer}")
			self.score += 1
		else:
			print(f"Wrong, The answers was {correct_answer}")
		print(f"Your score is {self.score}/{self.question_number}")
	