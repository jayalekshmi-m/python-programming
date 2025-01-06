myfile=open("name.txt","r")
myfile2=open("hi.txt","a")
line=myfile.readlines()
type(line)
for i in range(0,len(line)):
    if(i%2==0):
        myfile2.write(line[i])
    else:
        pass
myfile2.close()
myfile3=open("hi.txt","r")
line2=myfile3.read()
print(line2)
myfile.close()
myfile.close()
