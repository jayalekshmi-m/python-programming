a=int(input("Enter a number :"))
f=1
if a<0:
    print("Can't take the factorial ")
else:
    for i in range(1,a+1):
        f=f*i
print("The factorial of",a ,"=",f)
