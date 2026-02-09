#Reverse Three-Digit Number
num = int(input("Enter a three-digit number to reverse: "))
# Example: 123 -> 321
d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

reverse = (d3 * 100) + (d2 * 10) + d1
print(f"Reversed number: {reverse}")