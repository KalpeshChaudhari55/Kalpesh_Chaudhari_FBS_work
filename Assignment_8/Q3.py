#a.1 + 2 + 3 + ... + n
def sum_series_a(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n_val = int(input("Enter n for natural sum: "))
print("Sum of series:", sum_series_a(n_val))

# #b. 1! + 2! + 3! + ... + n!
def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

def sum_factorial_series(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n_val = int(input("Enter n for factorial sum: "))
print("Sum of factorial series:", sum_factorial_series(n_val))

# #c.1^1 + 2^2 + 3^3 + ... + n^n
def sum_power_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (i ** i)
    return total

n_val = int(input("Enter n for power series: "))
print("Sum of power series:", sum_power_series(n_val))