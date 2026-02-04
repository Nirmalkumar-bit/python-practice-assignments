# Goal: Determine triangle type based on side lengths.
# Rules:
# - If any side <= 0 OR triangle inequality fails -> Not a triangle
# - Else if all three sides equal -> Equilateral
# - Else if exactly two sides equal -> Isosceles
# - Else -> Scalene
# Expected outcome for a=2, b=2, c=3: Isosceles

a = 2
b = 2
c = 3

# TODO: Use if/elif/else to print exactly one of:
# "Not a triangle", "Equilateral", "Isosceles", "Scalene"

if  a <= 0 or b <= 0 or c <= 0 or (a + b <= c or a + c <= b or b + c <= a):
    print("Not a triangle")

# All sides equal
elif a == b == c:
    print("Equilateral")

# Exactly two sides equal
elif a == b or b == c or a == c:
    print("Isosceles")

# All sides different
else:
    print("Scalene")