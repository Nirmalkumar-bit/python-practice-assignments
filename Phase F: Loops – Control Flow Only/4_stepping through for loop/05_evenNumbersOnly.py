# Goal: Step through numbers 1..10 and print only evens.
# Expected outcome (exact lines):
# 2
# 4
# 6
# 8
# 10

for n in range(1, 11):
    if n%2 == 0:
        print(n)