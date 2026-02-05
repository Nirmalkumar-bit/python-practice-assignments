# Read an integer h. Print a right triangle of height h using '#'.
# Each line i (1-based) contains exactly i '#' characters.
# Example for h=4:
# #
# ##
# ###
# ####

h = int(input())


for i in range(1, h + 1):
    line = ""
    for j in range(i):
        line += "#"
    print(line)

