#Divisible by 7 and multiple of 5 (range)
start = int(input("Enter start: "))
end = int(input("Enter end: "))

i = start
while i <= end:
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    i = i + 1
