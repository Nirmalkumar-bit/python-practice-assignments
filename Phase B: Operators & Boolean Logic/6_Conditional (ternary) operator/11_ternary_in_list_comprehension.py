# Goal: Use a conditional (ternary) expression inside a list comprehension.
# For each number, produce "E" if even else "O".
# Expected outcome: Prints exactly: ['O', 'E', 'O', 'E']

nums = [1, 2, 3, 4]

labels = ["E" if n%2 == 0 else "O" for n in nums]

print(labels)
