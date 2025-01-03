def st(a):
    if(len(a)<2):
        return a
    else:
        return a[-1]+a[1: -1]+a[0]
str=input("Enter the string:")
re=st(str)
print("The string after exchanging the first and last character :",re)
        
