# Goal: Sort version strings correctly (e.g., '1.10' > '1.2').
# Expected outcome: versions_sorted must be ['1.2', '1.9', '1.10', '2.0'].
# Constraint: Implement comparison via a comparator function and cmp_to_key.

from functools import cmp_to_key

versions = ['1.9', '1.10', '1.2', '2.0']


def compare_versions(a, b):
    a_parts = [int(x) for x in a.split(".")]
    b_parts = [int(x) for x in b.split(".")]

    if a_parts < b_parts:
        return -1
    elif a_parts > b_parts:
        return 1
    else:
        return 0

versions_sorted = sorted(versions, key=cmp_to_key(compare_versions))

    # TODO: return -1 if a<b, 0 if a==b, 1 if a>b using numeric comparison of dot parts
    

# TODO: create versions_sorted using sorted() + cmp_to_key(compare_versions)

print(versions_sorted)
