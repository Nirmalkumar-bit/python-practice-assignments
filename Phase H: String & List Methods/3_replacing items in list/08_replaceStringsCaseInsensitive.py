# Goal: Replace all case-insensitive matches of 'yes' with 'Y'.
# Expected outcome: printing the list shows ['Y', 'no', 'Y', 'maybe', 'Y']

answers = ['Yes', 'no', 'YES', 'maybe', 'yes']

# TODO:
# Replace any element that equals 'yes' ignoring case with 'Y'.
# Keep other elements unchanged.
for i in range(len(answers)):
    if answers[i].lower() == 'yes':
        answers[i] = 'Y'
print(answers)
