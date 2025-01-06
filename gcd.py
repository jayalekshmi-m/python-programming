def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
num1=int(input("enter first number"))
num2=int(input("enter second number"))
result=gcd(num1,num2)
print(f"gcd of {num1} and {num2} is {result}")

# for calculating gcd of 2 numbers usin function



import math
num1=int(input("enter first number"))
num2=int(input("enter second number"))
result=math.gcd(num1,num2)
print(f"gcd is {result}")

#simpler method using built in function

