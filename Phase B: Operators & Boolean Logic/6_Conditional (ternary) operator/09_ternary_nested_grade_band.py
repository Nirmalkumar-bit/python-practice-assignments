# Goal: Use a nested conditional (ternary) expression to compute a letter grade.
# Rules: score>=90 -> "A", score>=80 -> "B", else -> "C".
# Expected outcome: Prints exactly: B

score = 84

grade = "A" if score >= 90 else "B" if score >= 80 else "c"

print(grade)
