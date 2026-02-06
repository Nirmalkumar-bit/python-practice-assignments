# Goal: Find the index of the highest score; if there is a tie, keep the earliest index.
# Expected outcome:
# Best index: 1
# Best score: 99

scores = [88, 99, 99, 70]

best_index = None
best_score = None

# TODO:
# Use enumerate to update best_score and best_index.
# On ties (score == best_score), do NOT update best_index.
best_index = None
best_score = None

for index, score in enumerate(scores):
    if best_score is None or score > best_score:
        best_score = score
        best_index = index

print(f"Best index: {best_index}")
print(f"Best score: {best_score}")
