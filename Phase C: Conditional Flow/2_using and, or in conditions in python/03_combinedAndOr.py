# Goal: Decide if a discount applies.
# Rule: discount applies if (is_student AND age < 26) OR is_veteran
# Expected outcome:
# With is_student=True, age=20, is_veteran=False => print exactly: DISCOUNT
# If you change age to 30 (keeping others the same) => print exactly: NO DISCOUNT

try:
    is_student
except NameError:
    is_student = True

try:
    age
except NameError:
    age = 20

try:
    is_veteran
except NameError:
    is_veteran = False

if (is_student and age < 26) or is_veteran:
    print("DISCOUNT")
else:
    print("NO DISCOUNT")
