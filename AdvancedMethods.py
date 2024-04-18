submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


# TASK 1: Find out which students both submitted their assignments and attended the class.

def common_members(submitted, attended):
    submitted_and_attended = [i for i in submitted if i in attended]
    return submitted_and_attended
print(f"Students who submitted the assignment and attended the class:{common_members(submitted, attended)}")

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted.sort()
attended.sort()
print(submitted == attended)


# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended_clone = attended.copy()
attended_clone.remove("Eve")
attended_clone.remove("Frank")
print(f"The updated attended list is: {attended_clone}")