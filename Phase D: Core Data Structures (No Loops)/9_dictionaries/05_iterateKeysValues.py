# Goal: Iterate through items and format output.
# Expected outcome when run:
# apples=3
# bananas=5
# cherries=2

inventory = {
    "apples": 3,
    "bananas": 5,
    "cherries": 2
}
for k, v in inventory.items():
    print(f"{k}={v}")
# TODO: loop through inventory items and print "<key>=<value>" per line
