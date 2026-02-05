# Read an integer n, then print the sum 1+2+...+n.
# Example: input: 4 -> output: 10

n = int(input())

total = 0
for k in range(1, n+1):
    total = total + k

print(total)
