student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
for student in student_scores:
  grade=student_scores[student]
  if grade>90:
    student_scores[student]="Outstanding"
  elif grade>80:
    student_scores[student]="Exceeds Expectations"
  elif grade>70:
    student_scores[student]="Acceptable"
  else:
    student_scores[student]="Fail"

print(student_scores)
# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
