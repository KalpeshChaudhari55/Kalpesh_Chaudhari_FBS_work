#Numbers not divisible by 2 and 3
n = int(input("Enter n: "))

i = 1
while i <= n:
    if i % 2 != 0 and i % 3 != 0:
        print(i)
    i = i + 1
