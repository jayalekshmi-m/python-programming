d={"pen":5,"pencil":8,"eraser":10}
asc=dict(sorted(d.items()))
desc=dict(sorted(d.items(),reverse=True))
print(f"in ascending order {asc}")
print(f"in descending order {desc}")


a={1:"string",2:"main",3:"jack"}
asc2=dict(sorted(a.items()))
desc2=dict(sorted(a.items(),reverse=True))
print(f"ascending order {asc2}")
print(f"descending order {desc2}")

b={'name1':'jaya','name2':'ammu','name3':'monu'}
asc3=dict(sorted(b.items(), key=lambda item: item[1]))
desc3=dict(sorted(b.items(), key=lambda item: item[1], reverse=True))
print(f"{asc3}")
print(f"{desc3}")

# sorting in dictionary