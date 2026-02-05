# Goal: Find the most frequent non-space character in a string.
# If there's a tie, choose the alphabetically smallest character.
# Expected outcome when run:
# a

s = "a b a c c"
counts = {}
for ch in s:
    if ch == " ":
        continue
    counts[ch] = counts.get(ch, 0) + 1

most_common = min(
    (ch for ch in counts),
    key=lambda ch: (-counts[ch], ch)
)


print(most_common)
