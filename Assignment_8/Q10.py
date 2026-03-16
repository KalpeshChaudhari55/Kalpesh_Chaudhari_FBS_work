def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

yr = int(input("Enter year: "))
print("Is Leap Year:", is_leap(yr))