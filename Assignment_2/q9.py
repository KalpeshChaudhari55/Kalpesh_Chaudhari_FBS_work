#Swap Two Numbers (Without Third Variable
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

x = x + y
y = x - y
x = x - y

print(f"After swap: X = {x}, Y = {y}")