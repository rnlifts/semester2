row=int(input("Enter the number of row: "))
column=int(input("Enter the number of column: "))

outer_list=[]
ilist=[]
for i in range(1,row+1):
    ilist=[]
    for j in range(1,column+1):
        ilist.append(1)
    outer_list.append(ilist)
for k in range(1,row+1):
    for l in range(1,column+1):
        ask=int(input(f"enter the numbe according to the order a{k}{l}: "))
        outer_list[k-1][l-1]=ask
for m in range(row):
    print(outer_list[m])