# Goal: Calculate ticket price with age and time-based pricing.
# Rules:
# - If age < 0 -> print "Invalid age"
# - Else determine base price:
#     - age <= 12 -> 8
#     - age <= 64 -> 12
#     - else -> 9
# - Then apply time discount:
#     - if show_time is "matinee" -> subtract 2 from base price
#     - elif show_time is "evening" -> no change
#     - else -> print "Invalid show time" (and do not print a price)
# Expected outcome for age=70, show_time="matinee": Ticket price: 7

age = 70
show_time = "matinee"  # "matinee" or "evening"

# TODO: Use if/elif/else to print exactly:
# "Invalid age" OR "Invalid show time" OR "Ticket price: <number>"

if age < 0:
    print("Invalid age")

else:
    # Determine base price
    if age <= 12:
        base_price = 8
    elif age <= 64:
        base_price = 12
    else:
        base_price = 9

    # Apply time-based pricing
    if show_time == "matinee":
        print(f"Ticket price: {base_price - 2}")
    elif show_time == "evening":
        print(f"Ticket price: {base_price}")
    else:
        print("Invalid show time")