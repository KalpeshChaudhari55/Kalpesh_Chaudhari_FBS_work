def calculate_circle_area(radius):
    pi = 3.14159
    return pi * (radius ** 2)

r = float(input("Enter radius: "))
print(f"Area of circle: {calculate_circle_area(r)}")