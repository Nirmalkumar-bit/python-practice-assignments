# Parse a key=value pair and print "key -> value".
# Expected outcome: prints mode -> debug

pair = "mode=debug"
key, value = pair.split("=")
print(f"{key} -> {value}")
