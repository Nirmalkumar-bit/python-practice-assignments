# Goal: Contrast immutable bytes with mutable bytearray.
# Expected outcome:
# - Prints: "bytes error: TypeError"
# - Prints: "bytearray after: bytearray(b'jello')"

b = b"hello"
ba = bytearray(b"hello")

try:
    b[0] = ord("j") 
    # TODO: attempt to change first byte of b to 'j'
    pass
except Exception as e:
    print("bytes error:", type(e).__name__)

# TODO: change first byte of ba to 'j' (ASCII)
ba[0] = ord("j")
print("bytearray after:", ba)
