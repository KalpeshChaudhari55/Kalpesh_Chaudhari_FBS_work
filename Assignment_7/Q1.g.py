# Pattern g: 1, 121, 12321, etc. [cite: 333-337]
for i in range(1, 6):
    # Ascending
    for j in range(1, i + 1):
        print(j, end=" ")
    # Descending
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()