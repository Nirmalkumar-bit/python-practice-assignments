# Goal: Step through nested loops to print grid coordinates.
# Expected outcome (exact lines):
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)

for row in range(2):
    for col in range(3):
        print("(" + str(row) + "," + str(col) + ")")
