num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("1.addition/n 2.subtraction/n 3.multiplication/n 4.division")
choice=int(input("enter one operation"))
if choice==1:
    sum=num1+num2
    print(f"sum={sum}")
elif choice==2:
    diff=num1-num2
    print(f"difference={diff}")
elif choice==3:
    product=num1*num2
    print(f"product={product}")
elif choice==4:
    if num2==0:
        print("zero division error")
    else:
        quotient=num1/num2
        print(f"quotient={quotient}")
else:
    print("invalid choice")

    # arithmetic operations