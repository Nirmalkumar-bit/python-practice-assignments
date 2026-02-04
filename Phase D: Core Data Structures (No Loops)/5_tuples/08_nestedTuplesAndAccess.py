# You have a tuple of (name, (age, city)). Extract and print:
# 1) the person's name
# 2) the city
# Each on its own line.
# Expected output:
# Ada
# London

person = ('Ada', (36, 'London'))

name = person[0]
city = person[1][1]

print(name)
print(city)
