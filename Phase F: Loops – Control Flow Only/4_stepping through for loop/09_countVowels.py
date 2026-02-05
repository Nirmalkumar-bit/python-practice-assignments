# Goal: Step through each character and count vowels.
# Expected outcome (exact lines):
# vowels: 5

text = "education"
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("vowels:", count)