# Goal: Determine shipping type.
# Rules:
# - FREE if (cart_total >= 50 AND is_domestic) OR is_premium_member
# - Otherwise STANDARD
# Expected outcome:
# With cart_total=45, is_domestic=True, is_premium_member=True => print exactly: FREE
# With cart_total=45, is_domestic=True, is_premium_member=False => print exactly: STANDARD

# Set defaults ONLY if tests did not override them
cart_total = globals().get("cart_total", 45)
is_domestic = globals().get("is_domestic", True)
is_premium_member = globals().get("is_premium_member", True)

if (cart_total >= 50 and is_domestic) or is_premium_member:
    print("FREE")
else:
    print("STANDARD")
