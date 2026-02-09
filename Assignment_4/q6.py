#Check prime number
num = int(input("Enter number: "))

i = 2
flag = 0

while i < num:
    if num % i == 0:
        flag = 1
        break
    i = i + 1

if flag == 0 and num > 1:
    print("Prime number")
else:
    print("Not prime number")
