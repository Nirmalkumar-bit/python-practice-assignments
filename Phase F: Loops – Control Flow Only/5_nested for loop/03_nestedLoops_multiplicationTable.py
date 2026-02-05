# Goal: Build a multiplication table (1..n) as aligned rows.
# Expected outcome when n=4 (each number width=2):
#  1  2  3  4
#  2  4  6  8
#  3  6  9 12
#  4  8 12 16

n = 4
cell_width = 2

table_lines = []
for row in range(1, n + 1):
    cells = []
    for col in range(1, n + 1):
        value = row * col
        cells.append(str(value).rjust(cell_width))
    table_lines.append(" ".join(cells))

# TODO: Use nested loops for row and col from 1..n.
# Compute row*col and format each cell right-aligned to cell_width.
# Separate cells with a single space.


print("\n".join(table_lines))