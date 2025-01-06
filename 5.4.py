file=open("details.csv")
lines=file.readlines()
file.close()
col=lines[0].split(",")
print("coloumns are")
for coloumn in col:
    print(coloumn)
c=int(input("enter the coloumn index to be displayed:"))
for line in lines:
    info=line.split(",")
    print(info[c])
