# Goal: Step through 1..7 and skip printing 4 using continue.
# Expected outcome (exact lines):
# 1
# 2
# 3
# 5
# 6
# 7

for n in range(1, 8):
    if n == 4:
        continue
    print(n)