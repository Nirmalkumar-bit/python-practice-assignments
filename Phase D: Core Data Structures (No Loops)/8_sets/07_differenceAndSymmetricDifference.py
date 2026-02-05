# Goal: Compute difference and symmetric difference.
# Expected outcome: It prints:
# A-B: {'a', 'b'}
# symdiff: {'a', 'b', 'e'}
# (Order may vary.)

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}

diff = A - B   # TODO: elements in A not in B
sym = A ^ B # TODO: elements in exactly one of A or B

print('A-B:', diff)
print('symdiff:', sym)
