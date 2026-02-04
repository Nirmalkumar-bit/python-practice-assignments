# Goal: Understand 'in' with dictionaries (keys by default).
# Expected outcome:
# - Prints exactly:
#   key_exists
#   value_missing


prices = {"apple": 1.50, "banana": 0.75}

if "apple" in prices:
    print("key_exists")

if 1.25 not in prices.values():
    print("value_missing")
else:
    print("value_exists")

