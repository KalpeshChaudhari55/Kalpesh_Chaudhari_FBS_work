#Display Grade based on 5 subject marks.
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
m4 = int(input("Enter mark 4: "))
m5 = int(input("Enter mark 5: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

if avg >= 60:
    print("First Class")
elif avg >= 50:
    print("Second Class")
elif avg >= 40:
    print("Pass Class")
else:
    print("Fail")
