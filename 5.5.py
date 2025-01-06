import csv
field_names=["no","name","age"]
data=[{"no":1,"name":"ammu","age":22},
      {"no":2,"name":"vismaya","age":22},
      {"no":3,"name":"amay","age":21}]
with open ("roll.csv","w") as csvf:
    write=csv.DictWriter(csvf,fieldnames=field_names)
    write.writeheader()
    write.writerows(data)
with open("roll.csv","r")as file:
    cs=csv.DictReader(file)
    for row in cs:
        print(row)
