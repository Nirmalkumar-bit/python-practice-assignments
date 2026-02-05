# Print all characters of the string below except vowels (a, e, i, o, u), preserving order.
# Use a for loop and continue.
# Expected outcome (exact):
# Pythn

text = "Python"
vowels = "aeiouAEIOU"

for ch in text:
     if ch in vowels:
        continue
    # TODO: if ch is a vowel, continue
    
     print(ch, end="")

print()
