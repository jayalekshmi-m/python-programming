a=int(input("Enter the 1st number :"))
b=int(input("Enter the 2nd number :"))
print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
op=int(input("Choose an option from above :"))
if op==1:
    s=a+b
    print("Sum of the numbers =",s)
elif op==2:
    d=a-b
    print("Difference of the numbers =",d)
elif op==3:
    m=a*b
    print("Product of the numbers =",m)
elif op==4:
    if b==0:
        print("Division is not possible")
    else:
        di=a/b
        print("Quotient of the numbers =",di)
else:
    print("Invalid input")
    
