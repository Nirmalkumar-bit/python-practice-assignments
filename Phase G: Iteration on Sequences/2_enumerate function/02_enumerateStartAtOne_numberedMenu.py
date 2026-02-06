# Goal: Use enumerate with a start value.
# Expected outcome:
# 1 - Home
# 2 - Settings
# 3 - Logout

items = ["Home", "Settings", "Logout"]

# TODO: Use enumerate(..., start=1) and print in the format: <number> - <item>
for index, item in enumerate(items, start=1):
    print(f"{index} - {item}")

