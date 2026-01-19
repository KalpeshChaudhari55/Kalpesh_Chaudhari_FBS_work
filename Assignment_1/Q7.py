#Roots of a Quadratic Equation.

import math

a = 4
b = 5
c = 3

D = b*b - 4*a*c

if D > 0:
    r1 = (-b + math.sqrt(D)) / (2*a)
    r2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are:", r1, "and", r2)

elif D == 0:
    r = -b / (2*a)
    print("Root is:", r)

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Roots are:", real, "+ i", imag, "and", real, "- i", imag)
