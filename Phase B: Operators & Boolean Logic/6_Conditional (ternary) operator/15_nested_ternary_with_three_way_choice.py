# Goal: Use a nested conditional (ternary) expression to categorize a number.
# Rules:
# - If x < 0 -> "negative"
# - Else if x == 0 -> "zero"
# - Else -> "positive"
# Expected outcome: Prints exactly: zero

x = 0

category = "negative" if x < 0 else "zero" if x == 0 else "positive"

print(category)
