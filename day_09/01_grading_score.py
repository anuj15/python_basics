student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.
for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif 80 >= student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    elif 90 >= student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)
