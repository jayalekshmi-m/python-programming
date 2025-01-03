import math
import cmath
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
e=b*b-4*a*c
if e<0:
    r1=(-b+cmath.sqrt(e)/2*a)
    r2=(-b-cmath.sqrt(e)/2*a)
    print("Roots are :",r1,r2)
elif e>0:
    r1=(-b+math.sqrt(e)/2*a)
    r2=(-b-math.sqrt(e)/2*a)
    print("Roots are :",r1,r2)
else:
    r=-b/2*a
    print("Root is",r)
    



