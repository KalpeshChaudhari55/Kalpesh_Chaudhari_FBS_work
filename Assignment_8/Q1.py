def calculate_rectangle_area(length, width):
    return length * width

l = float(input("Enter length: "))
w = float(input("Enter width: "))
print(f"Area of rectangle: {calculate_rectangle_area(l, w)}")