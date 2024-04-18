students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1 Filter out students who have grades below 80. Print the name, grade and activiy.

John = students[0], grades[0], activities[0]
Doe = students[1], grades[1], activities[1]
Jane = students[2], grades[2], activities[2]
Smith = students[3], grades[3], activities[3]

print(Jane)


# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved = students.copy()
students_approved.remove("Jane")


# Task 3: Print the list students_approved

print(students_approved)