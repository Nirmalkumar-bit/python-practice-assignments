# Build a list of only the even numbers from nums and print it.
# Expected outcome:
# [2, 4, 6]

nums = [1, 2, 3, 4, 5, 6]

evens = []
for n in nums:
    if n%2 == 0:
        evens.append(n)

print(evens)
