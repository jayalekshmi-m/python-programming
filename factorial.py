num1=int(input("enter a number"))
fact=1
if num1<0:
    print("cannot take factorial")
else:
    for i in range(1,num1+1):
        fact=fact*i
print(f"factorial of {num1}={fact}")

# factorial of a number