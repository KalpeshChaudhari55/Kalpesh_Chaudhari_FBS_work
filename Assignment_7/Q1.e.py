# Pattern e: Starts from i, goes to 2*i-1, then back to i
for i in range(1, 6):
    # Spaces for pyramid alignment
    print(" " * (5 - i), end="")
    # Ascending
    for j in range(i, 2 * i):
        print(j, end="")
    # Descending
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end="")
    print()