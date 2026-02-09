#Numbers divisible by a given number
n = int(input("Enter range limit: "))
d = int(input("Enter divisor: "))

i = 1
while i <= n:
    if i % d == 0:
        print(i)
    i = i + 1
