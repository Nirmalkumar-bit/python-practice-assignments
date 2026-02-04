# Task: Use concatenation (+) and repetition (*) to create a pattern.
# Expected outcome:
# - banner should be exactly: '---GO!---'

left = "-" * 3
center = "GO!" * 1
right = "-" * 3

banner = left + center + right
print(banner)
