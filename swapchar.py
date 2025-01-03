a=input("Enter  string 1 :")
b=input("Enter  string 2 :")
if (len(a)<2) or (len(b)<2):
    print("Can't peform swapping ")
else:
    r=b[0]+a[1: ]+""+a[0]+b[1: ]
print(" Strings after swapping the first letteers of the strings is \n", r)
