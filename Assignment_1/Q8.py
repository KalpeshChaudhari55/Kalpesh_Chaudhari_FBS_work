#Convert days into years, weeks and days.

days = 465

years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print("Years =", years)
print("Weeks =", weeks)
print("Days =", remaining_days)
