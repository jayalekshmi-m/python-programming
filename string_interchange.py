a=input("enter a word")
if len(a)>1:
    a=a[-1]+a[1:-1]+a[0]
print(f"after interchanging first and last character= {a}")

# interchanging first and last character in a string




def string(word):
    if len(word)<2:
        return word
    else:
        word=word[-1]+word[1:-1]+word[0]
        return word
a=input("enter a word")
result=string(a)
print(f"after interchanging:{result}")

# interchange using function
        
