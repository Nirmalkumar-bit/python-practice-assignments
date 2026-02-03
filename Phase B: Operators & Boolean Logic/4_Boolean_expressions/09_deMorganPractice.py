# Goal: Use De Morgan's laws to create equivalent boolean expressions.
# Expected outcome:
# It prints exactly:
# original: False
# equivalent: False
# match: True

is_hungry = True
has_food = True
has_time = False

# original means: NOT (has_food AND has_time)
original = has_food and has_time

# equivalent should be written WITHOUT a leading NOT applied to parentheses.
# Use only 'not' directly on variables and 'and'/'or'.
equivalent = has_food and has_time or is_hungry and has_time

match = (original == equivalent)

print("original:", original)
print("equivalent:", equivalent)
print("match:", match)
