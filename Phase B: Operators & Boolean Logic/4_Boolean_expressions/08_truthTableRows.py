# Goal: Compute specific rows of a truth table.
# Expected outcome:
# It prints exactly:
# row1: True
# row2: False
# row3: True

# Define A, B values for each row and compute expr = (A and not B) or (not A and B)
# TODO: Fill in A/B and expr for each row.

# Row 1: A=True, B=False
A1 = True
B1 = False
row1 = (A1 and not B1) or (not A1 and B1)

# Row 2: A=True, B=True
A2 = True
B2 = True
row2 = (A2 and not B2) or (not A2 and B2)


# Row 3: A=False, B=True
A3 = False
B3 = True
row3 = (A3 and not B3) or (not A3 and B3)


print("row1:", row1)
print("row2:", row2)
print("row3:", row3)
