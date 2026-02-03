# Goal: Use a conditional (ternary) expression to compute the absolute value of x.
# Expected outcome: Prints exactly: abs=12

x = -12

abs_x = x if x >= 0 else -x

print(f"abs={abs_x}")
