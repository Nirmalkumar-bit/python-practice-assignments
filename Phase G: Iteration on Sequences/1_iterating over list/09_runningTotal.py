# Create a list of running totals and print it.
# Expected outcome:
# [2, 5, 9, 10]

nums = [2, 3, 4, 1]

running = []
total = 0
for n in nums:
    total += n 
    running.append(total)

print(running)
