#Ticket amount calculation for 5 people
ticket = float(input("Enter ticket amount per person: "))
total = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        total += ticket * 0.70
    elif age > 59:
        total += ticket * 0.50
    else:
        total += ticket

print("Total Ticket Amount =", total)
