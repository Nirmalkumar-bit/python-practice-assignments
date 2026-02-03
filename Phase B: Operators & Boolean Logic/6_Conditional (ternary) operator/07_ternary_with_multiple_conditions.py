# Goal: Use a conditional (ternary) expression with and/or in the condition.
# If age is between 13 and 19 inclusive, label is "teen" else "not teen".
# Expected outcome: Prints exactly: teen

age = 19

label = "not teen" if 13 >= age <=19  else "teen"

print(label)
