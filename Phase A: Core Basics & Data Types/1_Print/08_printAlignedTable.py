# Goal: Print a simple aligned table with fixed-width columns.
# Expected output:
# Item      Qty
# Apples      3
# Bananas    12

# TODO: Complete the print statements so the spacing matches exactly.
# Hint: Use string alignment with a fixed width.
print(f"{'Item':<10}{'Qty':>3}")
print(f"{'Apples':<10}{'3':>3}")
print(f"{'Bananas':<10}{'12':>3}")