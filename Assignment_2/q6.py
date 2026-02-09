#WAP TO CLACULATE TOTAL SALARY OF AN EMPLOYEE BASED ON BASIC , DA = 10% OF BASIC , HRA = 12% OF BASIC, TA = 12% OF BASIC
basicsal = float(input("Enter the basic salary: "))

da = basicsal * 0.10
hra = basicsal * 0.12
ta = basicsal * 0.12

totalsal = basicsal + da + hra + ta

print(f"Basic Salary: {basicsal}")
print(f"DA: {da}")
print(f"HRA: {hra}")
print(f"TA: {ta}")
print(f"Total Salary: {totalsal}")