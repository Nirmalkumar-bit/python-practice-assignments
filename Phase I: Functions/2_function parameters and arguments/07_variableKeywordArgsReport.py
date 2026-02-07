# Goal: Practice **kwargs.
# Expected outcome: Running the file prints exactly:
# age=12; name=Ria

# TODO: Define report(**fields) that returns key=value pairs sorted by key
# joined by "; ".
# Example: report(name="Ria", age=12) -> "age=12; name=Ria"

def report(**fields):
    parts = []
    for key in sorted(fields):
        parts.append(f"{key}={fields[key]}")
    return "; ".join(parts)

    
    

print(report(name="Ria", age=12))
