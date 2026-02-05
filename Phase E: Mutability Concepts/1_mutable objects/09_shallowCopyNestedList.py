# Goal: Observe shallow copy behavior with nested lists.
# Expected outcome: prints exactly:
# original: [[1, 99], [3, 4]]
# shallow: [[1, 99], [3, 4]]


def main():
    original = [[1, 2], [3, 4]]
    shallow = original.copy()      # shallow copy (outer list only)
    shallow[0][1] = 99  

    # TODO: make a shallow copy of original (outer list only)
    

    # TODO: mutate the first inner list so that 2 becomes 99

    print("original:", original)
    print("shallow:", shallow)


if __name__ == "__main__":
    main()
