# Goal: use append, extend, and insert correctly.
# Expected outcome (print output):
# ["start", "a", "b", "c", "end"]

items = ["a", "b"]

# TODO: insert "start" at the beginning
items.insert(0, "start")
# TODO: append "end" to the end
items.extend("c")
items.append("end")
# TODO: extend with ["c"] so the final list matches the expected output


print(items)
