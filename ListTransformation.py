# TASK 1  grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

# TASK 2 Calculate the average grade and display it.

average = sum(grades) / len(grades)
print(f"Average grade = {average}%")

# Task 3: Replace any grade below 80 with the value Failed.

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
print(grades)