# Pattern f: 1...1, 12...21, etc.
for i in range(1, 5):
    # Left side
    for j in range(1, i + 1):
        print(j, end="")
    # Gap between sides
    print(" " * (8 - 2 * i), end="")
    # Right side
    for j in range(i, 0, -1):
        print(j, end="")
    print()