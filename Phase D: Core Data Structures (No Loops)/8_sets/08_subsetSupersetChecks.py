# Goal: Check subset and superset relationships.
# Expected outcome: It prints:
# True
# False
# True

small = {2, 4}
big = {1, 2, 3, 4, 5}
other = {4, 6}

print(small <= big)    # small is subset of big
print(other <= big)    # other is subset of big
print(big >= small)    # big is superset of small

