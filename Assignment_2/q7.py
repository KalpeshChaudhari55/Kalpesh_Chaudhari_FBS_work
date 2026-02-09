#Sum of Three-Digit Number
num = int(input("Enter a three-digit number: "))
# Example: 123 -> 1+2+3 = 6
sum_digits = (num // 100) + ((num // 10) % 10) + (num % 10)
print(f"Sum of digits: {sum_digits}")