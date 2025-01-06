col=input("enter a list of colors separated by commas")
# col[1]=col[-1]
# col[-1]=col[1]
col_list=col.split(',')
print(f"first color {col_list[-1]}")
print(f"last color {col_list[1]}")

#interchanging first and last color in a list