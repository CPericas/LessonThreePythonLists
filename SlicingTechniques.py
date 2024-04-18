temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1: Extract the temperatures for the second week (7 days) of the month.

temperatures = temperatures[:6] + temperatures[13:]
print(temperatures)

# Task 2: Extract all the temperatures above 100.

temperatures = temperatures[:-6]
print(temperatures)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.reverse()
temperatures = temperatures[:4] + temperatures[10:]
print(temperatures)