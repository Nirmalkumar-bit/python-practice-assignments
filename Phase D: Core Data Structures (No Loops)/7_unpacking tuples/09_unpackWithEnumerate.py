# Use enumerate with unpacking to label each item. Start counting at 1.

names = ("Ada", "Linus", "Grace")

lines = []
for i, name in enumerate(names, start=1):
    lines.append(f"{i}: {name}")
# TODO: loop with enumerate(names, start=1) and unpack (i, name)
# Append lines like "1: Ada" to lines

print("\n".join(lines))
# Expected outcome:
# 1: Ada
# 2: Linus
# 3: Grace
