# Goal: Build an immutable, hashable composite key from nested data.
# Expected outcome:
# - Prints: "key hashable: True"
# - Prints: "lookup: found"

user = {
    "name": "Ada",
    "roles": ["admin", "editor"],
    "region": "EU"
}

# TODO: create an immutable key using (name, tuple(roles), region)


key = (user["name"], tuple(user["roles"]), user["region"])

cache = {key: "found"}

try:
    hash(key)
    key_hashable = True
except Exception:
    key_hashable = False
# TODO: create a dict cache mapping key -> "found"


# TODO: set key_hashable to True if hash(key) works without raising


print("key hashable:", key_hashable)
print("lookup:", cache.get(key))
