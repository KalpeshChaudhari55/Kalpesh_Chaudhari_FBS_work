#convert distant given in feet and inches into meter and centimeter 
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

meters = feet * 0.3048
centimeters = inches * 2.54
print(f"Distance: {meters} meters and {centimeters} centimeters")