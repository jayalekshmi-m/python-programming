s=input("Enter the string :")
a=input("Enter the letter to be searched :")
c=0
for i in s:
    if a==i:
        c+=1
print("Count is :",c)
