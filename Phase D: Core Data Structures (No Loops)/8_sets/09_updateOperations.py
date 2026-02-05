# Goal: Use in-place set update operations.
# Expected outcome: It prints:
# {1, 2, 3, 4, 5}
# {3, 4, 5}
# (Order may vary.)

s = {1, 2, 3}
s.update({3, 4, 5}) # TODO: update s with {3, 4, 5} so s becomes {1,2,3,4,5}
print(s)

s.intersection_update({3, 4, 5, 6})  # TODO: intersect-update s with {3, 4, 5, 6} so s becomes {3,4,5}
print(s)
