#Perfect number
num = int(input("Enter number: "))

sum = 0
i = 1

while i < num:
    if num % i == 0:
        sum = sum + i
    i = i + 1

if sum == num:
    print("Perfect number")
else:
    print("Not perfect number")
