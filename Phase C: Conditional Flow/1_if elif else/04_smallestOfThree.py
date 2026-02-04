# Goal: Print the smallest of three numbers.
# Expected outcome for a=8, b=3, c=5: 3

a = 8
b = 3
c = 5

# TODO: Use if/elif/else to determine and print the smallest value
# Constraint: Do not use min().

if a < b and a < c:
    print(a)
elif b < a and  b < c:
    print(b)
else:
    print(c)