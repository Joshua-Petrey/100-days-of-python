scores = input("What are the student scores?").split()

highest_score = None
for score in scores:
	if highest_score == None or highest_score < int(score):
		highest_score = int(score)
print(highest_score)

# Or just use max() to solve
print(max(scores))