# Goal: Implement a stable sort (do not use list.sort() or sorted()).
# Task: Write stable_sort_by_key(items, key_func) that returns a NEW list.
# Constraint: Must be stable (original order preserved for equal keys).
# Hint: Implement merge sort.
# Expected outcome:
# When sorting by score ascending, the returned list must be:
# [('Ben', 2), ('Dan', 2), ('Ava', 3), ('Cara', 3)]
# (Ben must stay before Dan; Ava must stay before Cara).

def stable_sort_by_key(items, key_func):
    if len(items) <= 1:
        return items[:]

    mid = len(items) // 2

    left = stable_sort_by_key(items[:mid], key_func)
    right = stable_sort_by_key(items[mid:], key_func)

    # Merge step (this is where stability is enforced)
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            # <= guarantees stability (left item wins ties)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining items
    result.extend(left[i:])
    result.extend(right[j:])

    return result


pairs = [('Ava', 3), ('Ben', 2), ('Cara', 3), ('Dan', 2)]

sorted_pairs = stable_sort_by_key(pairs, key_func=lambda x: x[1])

print(sorted_pairs)
    # TODO: implement stable merge sort that uses key_func
    # Do NOT mutate the input list.
    

# TODO: call stable_sort_by_key with key_func that extracts the score

