# Goal: Prefix each row with its row number (starting at 1) using enumerate.
# Expected outcome:
# [[1, 'Ann'], [2, 'Ben'], [3, 'Cy']]

table = [["Ann"], ["Ben"], ["Cy"]]

# TODO: Modify each inner list in-place to insert row number at position 0.

for index, row in enumerate(table, start=1):
    row.insert(0, index)


print(table)
