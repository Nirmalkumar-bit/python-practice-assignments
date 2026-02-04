# Goal: Print an alert category based on temperature and humidity.
# Rules:
# - Print DANGER if temperature >= 40 OR (temperature >= 35 AND humidity >= 70)
# - Else print OK
# Expected outcome:
# With temperature=36, humidity=75 => print exactly: DANGER
# With temperature=34, humidity=80 => print exactly: OK

try:
    temperature
except NameError:
    temperature = 46

try:
    humidity
except NameError:
    humidity = 80


if temperature >= 40 or (temperature >= 35 and humidity >= 70):
    print("DANGER")
else:
    print("OK")
