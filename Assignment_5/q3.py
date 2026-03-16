# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
n = int(input("enter the number of passengers: "))
cost = float(input("enter the per ticket cost: "))
total_amount = 0
price = 0

for i in range(n):
    age = int(input("enter the age of passenger: "))
    
    if age < 12:
        price = cost * 0.70
    elif age > 59:
        price = cost * 0.50
    else:
        price = cost

    total_amount = total_amount + price

print("total amount:", total_amount)