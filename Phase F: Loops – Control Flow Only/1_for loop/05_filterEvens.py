# Build a list containing only the even numbers from nums using a for loop.
# Expected outcome: print [2, 8, 0, -4]

nums = [3, 2, 5, 8, 1, 0, -4]
evens = []

# TODO: Append only even numbers to evens
for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)
