#Check 3-digit Palindrome number.
num = int(input("Enter a 3 digit number: "))

rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
