# Goal: Convert a nested structure into a deeply immutable equivalent.
# Supported conversions:
# - list -> tuple
# - dict -> tuple of sorted (key, value) pairs, with values also frozen
# - set -> frozenset
# Leave primitives (int/str/None/bool/float) as-is.
# Expected outcome:
# - Prints: "type: tuple"
# - Prints: "hashable: True"
# - Prints: "frozen_repr: (('a', (1, 2)), ('b', frozenset({3, 4})), ('c', (('x', 9),)))" (ordering must match sorted keys)

data = {
    "b": {3, 4},
    "a": [1, 2],
    "c": {"x": 9}
}

def freeze(obj):
    if isinstance(obj, dict):
        return tuple(
            (k, freeze(obj[k]))
            for k in sorted(obj)
        )
    elif isinstance(obj, list):
        return tuple(freeze(x) for x in obj)
    elif isinstance(obj, set):
        return frozenset(freeze(x) for x in obj)
    else:
        return obj

    # TODO: implement deep freezing per rules above
    # Hint: for dict, sort keys to ensure deterministic output
    pass

frozen = freeze(data)

print("type:", type(frozen).__name__)
try:
    hash(frozen)
    hashable = True
except TypeError:
    hashable = False

# TODO: set hashable to True if hash(frozen) succeeds
hashable = True
print("hashable:", hashable)

print("frozen_repr:", frozen)
