# Parse a log line and extract date, level, and message.
# Expected outcome: prints 2026-02-02 WARNING Disk almost full

log = "2026-02-02|WARNING|Disk almost full"
parts = log.split("|")
# Assign date, level, message from parts
date , level, message = parts
print(date, level, message)
