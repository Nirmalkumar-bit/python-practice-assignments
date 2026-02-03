# Goal: Use a conditional (ternary) expression where each branch performs a calculation.
# If minutes > 60, compute hours=minutes/60 else hours=0.
# Expected outcome: Prints exactly: hours=1.5

minutes = 90

hours =  hours=minutes/60 if minutes > 60 else 0

print(f"hours={hours}")
