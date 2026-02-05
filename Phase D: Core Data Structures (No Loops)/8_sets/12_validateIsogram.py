# Goal: Determine if a word is an isogram (no repeated letters), ignoring hyphens and spaces.
# Expected outcome: It prints:
# True
# False

word1 = 'six-year'
word2 = 'programming'

def is_isogram(text: str) -> bool:
    cleaned =text.lower().replace('-', '').replace(' ', '')   # TODO: lowercase text and remove '-' and spaces
    letters =  [c for c in cleaned if c.isalpha()]  # TODO: build a list or iterable of alphabetic characters only
    return len(letters) == len(set(letters))  # TODO: True if no repeats, else False

print(is_isogram(word1))
print(is_isogram(word2))
