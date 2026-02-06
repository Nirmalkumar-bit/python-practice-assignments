# Convert each word to uppercase, then join them with '-' and print.
# Expected outcome:
# CAT-DOG-FISH

animals = ["cat", "dog", "fish"]

upper_animals = []
for a in animals:
    upper_animals.append(a.upper())

print("-".join(upper_animals))
