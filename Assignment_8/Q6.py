def print_fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

terms = int(input("Enter number of Fibonacci terms: "))
print_fibonacci(terms)