# Goal: Find people who attended both events.
# Expected outcome: It prints a set containing exactly {'Ava', 'Noah'} (order may vary).

event1 = {'Ava', 'Noah', 'Mia', 'Liam'}
event2 = {'Noah', 'Ava', 'Ethan'}

both = event1&event2 # TODO: compute intersection
print(both)
