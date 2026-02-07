# Task: Implement remove_punctuation(s) that removes ',', '.', '!' characters.
# Implement collapse_spaces(s) that turns runs of whitespace into a single space.
# Implement clean_sentence(s) that calls remove_punctuation then collapse_spaces then strips ends.
# Expected outcome: print(clean_sentence(" Hi,,  world!!  ")) outputs exactly: Hi world

def remove_punctuation(s):
     for ch in ",.!":
        s = s.replace(ch, "")
     return s

    # TODO
    


def collapse_spaces(s):
     return " ".join(s.split())

    # TODO
    

def clean_sentence(s):
    s = remove_punctuation(s)
    s = collapse_spaces(s)
    return s.strip()

    # TODO: call helpers in the correct order
    


print(clean_sentence(" Hi,,  world!!  "))
