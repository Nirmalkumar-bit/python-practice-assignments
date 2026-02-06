# Goal: Replace items in one list based on a mapping defined by two parallel lists.
# Replace any fruit found in old_names with the corresponding item in new_names.
# Expected outcome: printing the list shows ['banana', 'orange', 'kiwi', 'orange', 'banana']

basket = ['apple', 'orange', 'kiwi', 'orange', 'apple']
old_names = ['apple']
new_names = ['banana']

# TODO:
# For each element in basket, if it exists in old_names, replace it with the matching element in new_names.
# Do this in place.

for i in range(len(basket)):
    if basket[i] in old_names:
        idx = old_names.index(basket[i])
        basket[i] = new_names[idx]

print(basket)
