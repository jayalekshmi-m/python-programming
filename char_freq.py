a=input("enter a word")
b=input("enter the letter to search")
count=0
for i in a:
    if(i==b):
        count=count+1
print(f"frequency of {b} is {count}")

# character frequency in a string
