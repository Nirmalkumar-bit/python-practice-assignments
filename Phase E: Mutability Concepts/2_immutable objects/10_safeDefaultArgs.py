# Goal: Use an immutable default argument safely.
# Expected outcome:
# - Prints exactly:
#   ()
#   (1,)
#   ()

def add_item(item, items=()):
    return items if item is None else items + (item,)

    """Return a NEW tuple containing previous items plus item."""
    # TODO: implement by returning a new tuple
    pass

print(add_item(None))
print(add_item(1))
print(add_item(None))
