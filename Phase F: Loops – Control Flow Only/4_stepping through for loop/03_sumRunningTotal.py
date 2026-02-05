# Goal: Step through the loop and track a running total.
# Expected outcome (exact lines):
# total: 15

total = 0
for n in range(1, 6):
    total = total + n
print("total:", total)