# Safely remove an item that may or may not exist
# Goal: Try to remove 'kiwi' from fruits.
# If 'kiwi' is not present, do nothing.
# Expected output:
# fruits: ['apple', 'banana', 'mango']

fruits = ['apple', 'banana', 'mango']

# TODO: attempt to remove 'kiwi' without crashing
# Constraint: Use try/except with list.remove
# safely attempt to remove 'kiwi'
try:
    fruits.remove('kiwi')
except ValueError:
    pass
print('fruits:', fruits)
