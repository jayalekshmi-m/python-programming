arr = list(map(int, input("Enter list elements separated by space: ").split()))
arr = [i for i in arr if i % 2 != 0]
print(f"list after removing even numbers {arr}")

# removing even numbers in list using user input


l=[1,2,3,4,5,6,7,8,9]
for i in l:
    if i%2==0:
        l.remove(i)
print(f"list after removing even numbers is {l}")

