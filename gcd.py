def gcd(a,b):
    if(b==0):
        print("GCD = ",a)
    else:
        return gcd(b,a%b)
e=int(input("Enter a :"))
d=int(input("Enter b :"))
gcd(e,d)

