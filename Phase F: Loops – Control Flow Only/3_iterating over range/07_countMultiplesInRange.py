# Read integers a, b, and m (in that order).
# Count how many integers in the inclusive range [a, b] are divisible by m.
# Print only the count.
# Example: a=3, b=10, m=2 -> output: 4 (4,6,8,10)

a = int(input())
b = int(input())
m = int(input())


count = 0
for n in range(a, b + 1):
    if n % m == 0:
        count += 1

print(count)


