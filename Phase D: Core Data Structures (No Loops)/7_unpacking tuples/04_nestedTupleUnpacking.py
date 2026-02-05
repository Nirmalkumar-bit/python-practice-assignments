# Unpack a nested tuple to extract city and zip code, then print them.

address = ("Ava", ("Austin", "TX"), 78701)

# TODO: unpack to get city and zip_code only (ignore other pieces)
city = address[1][0]
zip_code = address[2]
print(city)
print(zip_code)
# Expected outcome:
# Austin
# 78701
