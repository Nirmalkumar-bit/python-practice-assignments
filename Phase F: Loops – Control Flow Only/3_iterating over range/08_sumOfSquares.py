# Read an integer n. Print the sum of squares from 1^2 to n^2.
# Example: n=3 -> output: 14

n = int(input())

total = 0
for k in range(1, n + 1):
    total += k * k

print(total)
