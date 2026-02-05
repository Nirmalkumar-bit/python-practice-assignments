# Use nested for loops to print a 3x4 grid of '*' characters (no spaces).
# Expected outcome (exactly):
# ****
# ****
# ****

rows = 3
cols = 4

# TODO: Use nested loops; each row should be printed on its own line
# Use nested loops; each row should be printed on its own line
for r in range(rows):
    line = ""
    for c in range(cols):
        line = line + "*"
    print(line)
