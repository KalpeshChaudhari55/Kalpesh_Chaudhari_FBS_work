def is_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10
    return total == original

val = int(input("Enter number to check Armstrong: "))
print("Is Armstrong Number:", is_armstrong(val))