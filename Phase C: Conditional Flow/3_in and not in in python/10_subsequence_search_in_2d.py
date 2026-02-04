# Goal: Use 'in' / 'not in' in a more complex setting: seat availability in a 2D grid.
# Seats are labeled like 'A1', 'A2', ... rows A-C and columns 1-4.
# Some seats are reserved; determine which requested seats are available.
# Expected outcome:
# - Prints exactly:
#   available: ['A1', 'B4']
#   unavailable: ['A2', 'C3']

rows = ["A", "B", "C"]
cols = [1, 2, 3, 4]

reserved = {"A2", "C3", "B1"}
requested = ["A1", "A2", "B4", "C3"]

rows = ["A", "B", "C"]
cols = [1, 2, 3, 4]

reserved = {"A2", "C3", "B1"}
requested = ["A1", "A2", "B4", "C3"]

valid_seats = set()
for r in rows:
    for c in cols:
        valid_seats.add(f"{r}{c}")

available = []
unavailable = []

for seat in requested:
    if seat in valid_seats and seat not in reserved:
        available.append(seat)
    else:
        unavailable.append(seat)

print(f"available: {available}")
print(f"unavailable: {unavailable}")

