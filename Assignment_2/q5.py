# selling price calcualtor 
cp = float(input("Enter cost price: "))
discount_per = float(input("Enter discount percentage: "))

discount_amt = (discount_per / 100) * cp
sp = cp - discount_amt
print(f"Selling Price: {sp}")