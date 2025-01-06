def fact(n):
    if n<0:
        print("cannot take factorial")
        return None
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
num=int(input("enter a number"))
result=fact(num)
if result is not None:
    print(f"factorial of {num} is {result}")

    # taking factorial using function