# Goal: Print grid coordinates using nested loops.
# Expected outcome when width=3 and height=2:
# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)

width = 3
height = 2

lines = []
for y in range(height):
    line_parts = []
    for x in range(width):
        line_parts.append(f"({x},{y})")
    lines.append(" ".join(line_parts))

# TODO: Use nested loops over y then x.
# For each row y, create a line with coordinates separated by a single space.
# Append each completed line to lines.


print("\n".join(lines))