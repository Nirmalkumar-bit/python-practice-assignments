# Goal: Use a conditional (ternary) expression to avoid dividing by zero.
# If denominator == 0, result should be "undefined" else compute numerator/denominator.
# Expected outcome: Prints exactly: undefined

numerator = 10
denominator = 0

result = "undefined" if denominator == 0 else numerator / denominator

print(result)
