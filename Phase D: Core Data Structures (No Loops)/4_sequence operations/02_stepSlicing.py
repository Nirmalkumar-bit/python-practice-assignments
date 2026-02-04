# Task: Use slicing with a step to build derived strings.
# Expected outcome:
# - evens should be '02468'
# - odds should be '13579'
# - reversed_digits should be '9876543210'

digits = "0123456789"

evens = digits[: :2]
odds = digits[1::2]
reversed_digits = digits[::-1]

print(evens)
print(odds)
print(reversed_digits)
