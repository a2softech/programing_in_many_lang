# 2. Python Program to Solve Quadratic Equations


from math import sqrt
a,b,c = 1,-2,-15

dpos = (-b + sqrt((b**2) - 4*a*c))/ (2*a)
dneg = (-b - sqrt((b**2) - 4*a*c))/ (2*a)

print(dpos,dneg)