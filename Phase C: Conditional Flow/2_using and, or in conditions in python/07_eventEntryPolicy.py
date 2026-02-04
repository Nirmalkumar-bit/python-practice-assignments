# Goal: Determine if someone can enter an event.
# Rules:
# - Must have ticket.
# - If age < 18, must also be accompanied.
# - VIPs can enter without a ticket only if they are on the guest list.
# Print exactly: ENTER or DENY
# Expected outcome:
# With has_ticket=False, is_vip=True, on_guest_list=True, age=25, accompanied=False => ENTER
# With has_ticket=True, is_vip=False, on_guest_list=False, age=16, accompanied=False => DENY

has_ticket = globals().get("has_ticket", False)
is_vip = globals().get("is_vip", True)
on_guest_list = globals().get("on_guest_list", True)
age = globals().get("age", 25)
accompanied = globals().get("accompanied", False)

regular_entry = has_ticket and (age >= 18 or accompanied)
vip_entry = is_vip and on_guest_list

if regular_entry or vip_entry:
    print("ENTER")
else:
    print("DENY")
