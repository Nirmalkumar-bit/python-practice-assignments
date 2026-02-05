# Goal: Given a positive integer n, repeatedly apply:
# - if n is even: n = n // 2
# - else: n = 3*n + 1
# Stop when n becomes 1. Count how many steps it takes and print the step count.
# For n = 6, sequence is 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1, so steps = 8
# Expected outcome (exact line):
# Steps: 8

n = 6
steps = 0

# TODO: implement Collatz with a while loop

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps = steps + 1


print("Steps:", steps)
