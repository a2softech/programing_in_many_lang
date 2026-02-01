# 2. Python Program to Solve Quadratic Equations

from math import sqrt
a,b,c = 4,3,2

dpos=-b+(((b**2)-(4*a*c))*0.5)/2*a
dneg=-b-(((b**2)-(4*a*c))*0.5)/2*a

print(dpos,dneg)
