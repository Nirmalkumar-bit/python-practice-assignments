# Goal: Show that string concatenation produces a new object.
# Expected outcome:
# - Prints: "original: hello"
# - Prints: "new: hello world"
# - Prints: "same object? False"

s = "hello"
# TODO: capture original object id
orig_id = id(s)

# TODO: create t by adding " world" to s without modifying s
t = s + " world"


print("original:", s)
print("new:", t)
print("same object?", id(s) == id(t))
