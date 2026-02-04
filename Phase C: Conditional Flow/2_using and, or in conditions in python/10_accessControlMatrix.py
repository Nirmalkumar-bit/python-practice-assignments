# Goal: Determine access level for a system based on multiple inputs.
# Rules (in order):
# 1) If is_suspended is True => print NO ACCESS
# 2) Else if (role is 'admin') OR (role is 'staff' AND has_2fa AND is_on_network) => print FULL ACCESS
# 3) Else if (role is 'guest' AND has_invite) OR (role is 'staff' AND has_2fa) => print LIMITED ACCESS
# 4) Else => print NO ACCESS
# Expected outcome:
# With role='staff', has_2fa=True, is_on_network=False, has_invite=False, is_suspended=False => LIMITED ACCESS
# If you change is_on_network=True (keeping others same) => FULL ACCESS

role = globals().get("role", "staff")
has_2fa = globals().get("has_2fa", True)
is_on_network = globals().get("is_on_network", False)
has_invite = globals().get("has_invite", False)
is_suspended = globals().get("is_suspended", False)

if is_suspended:
    print("NO ACCESS")
elif role == "admin" or (role == "staff" and has_2fa and is_on_network):
    print("FULL ACCESS")
elif (role == "guest" and has_invite) or (role == "staff" and has_2fa):
    print("LIMITED ACCESS")
else:
    print("NO ACCESS")
