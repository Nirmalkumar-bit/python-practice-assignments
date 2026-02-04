# Goal: Convert a numeric score (0-100) into a letter grade.
# Rules:
# - 90-100: A
# - 80-89: B
# - 70-79: C
# - 60-69: D
# - 0-59: F
# Expected outcome for score=83: B

score = 83

# TODO: Use if/elif/else to print exactly one letter grade
# NOTE: You may assume score is between 0 and 100 for this assignment.

if 100 > score >90:
    print("A")
elif 89 > score > 80:
    print("B")
elif 79 > score >70:
    print("c")
elif 69 > score > 60:
    print("D")
else:
    print("F")