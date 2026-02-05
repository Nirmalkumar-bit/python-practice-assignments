# Goal: Print a right triangle of increasing numbers per row.
# Expected outcome when rows=5:
# 1
# 12
# 123
# 1234
# 12345

rows = 5

lines = []
for i in range(1, rows + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    lines.append(line)


# TODO: Use nested loops.
# Outer loop for each row i (1..rows)
# Inner loop to append numbers 1..i into a string.


print("\n".join(lines))