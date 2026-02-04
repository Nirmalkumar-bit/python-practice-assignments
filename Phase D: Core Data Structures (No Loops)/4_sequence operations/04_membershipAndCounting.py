# Task: Use membership (in / not in) and sequence methods for counting.
# Expected outcome:
# - has_a should be True
# - has_z should be False
# - count_a should be 6

text = "bananas and avocados"

has_a = "a" in text
has_z = "z" in text
count_a = text.count("a")

print(has_a)
print(has_z)
print(count_a)
