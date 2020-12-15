student_scores = {
	"Harry": 81,
  	"Ron": 78,
  	"Hermione": 99, 
  	"Draco": 74,
  	"Neville": 62,
}

student_grades = {}

for x in student_scores:
	if student_scores[x] <= 70:
		student_grades[x] = "Fail"
	elif student_scores[x] <= 80:
		student_grades[x] = "Acceptable"
	elif student_scores[x] <= 90:
		student_grades[x] = "Exceeds expectations"
	else:
		student_grades[x] = "Outstanding"
		
print(student_grades)