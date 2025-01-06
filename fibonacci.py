def fibo(n):
    if n<=0:
        print("pls enter positive integer")
        return None 
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_series=[0,1]
        for i in range(2,n):
            next_series=fib_series[-1]+fib_series[-2]
            fib_series.append(next_series)
        return fib_series
num=int(input("enter number of terms"))
result=fibo(num)
if result is not None:
    print(f"{result}")

    # fibonacci series of a number