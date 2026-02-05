# Goal: Use a set comprehension to generate unique squares for numbers in a list.
# Expected outcome: It prints a set containing exactly {0, 1, 4, 9, 16} (order may vary).

nums = [0, 1, 2, 2, 3, 4, 4]
squares = {n * n for n in nums} # TODO: set comprehension of n*n for each n in nums
print(squares)
