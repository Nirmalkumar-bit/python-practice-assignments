# Goal: Unpack a nested tuple into named variables
# Expected outcome: running this file prints exactly: Jane 34 NY

record = ("Jane", (34, "NY"))

# TODO: unpack record into name, age, state
name = record[0]
age = record[1][0]
state = record[1][1]

print(name, age, state)
