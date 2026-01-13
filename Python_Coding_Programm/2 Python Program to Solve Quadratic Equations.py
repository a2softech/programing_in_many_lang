# Python Program to Solve Quadratic Equations
import math
a,b,c = 1,-5,6

d1 = ((-b)+math.sqrt(b**2-4*a*c))/2*a
d2 = ((-b)-math.sqrt(b**2-4*a*c))/2*a

print(d1)
print(d2)