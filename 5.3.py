import csv as hl
with open("new.csv") as h:
    read=hl.reader(h)
    for lines in read:
        print(lines)
