def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def sum_primes(n):
    total = 0
    for i in range(1, n + 1):
        if is_prime(i):
            total += i
    return total

limit = int(input("Enter n for prime sum: "))
print("Sum of prime numbers:", sum_primes(limit))