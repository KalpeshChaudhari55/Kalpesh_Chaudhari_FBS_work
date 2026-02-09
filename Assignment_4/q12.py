#Armstrong number
num = int(input("Enter number: "))

temp = num
sum = 0
digits = 0

t = num
while t > 0:
    digits = digits + 1
    t = t // 10

while temp > 0:
    digit = temp % 10
    power = 1
    i = 1
    while i <= digits:
        power = power * digit
        i = i + 1

    sum = sum + power
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")
