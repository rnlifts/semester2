# code for first matrix
def add_matrix():
    row = int(input("enter number of row for first matrix: "))
    column = int(input("enter number of column for first matrix: "))

    #creating a temporary matrix
    outer_List = []
    ilist = []

    for i in range(row):
        ilist = []
        for j in range(column):
            ilist.append("*")
        outer_List.append(ilist)

    #replacing temporary matrix with the matrix provided by user 
    for a in range(1,row+1):  
     for b in range(1,column+1):
        ab=a;
        bc=b;
        hello=int(input(f"enter the order a{ab}{bc} "))
        outer_List[ab-1][bc-1]=hello;
    for k in range(row):
     print(outer_List[k])
        
    # code for second matrix
    row2= int(input("enter no. of row for second matrix: "))
    column2 = int(input("enter no. of column for second matrix: "))
    outer_List2 = []
    ilist2 = []

    #creating temporary matrix
    for i2 in range(row2):
        ilist2 = []
        for j2 in range(column2):
            ilist2.append("*")
        outer_List2.append(ilist2)

    #replacing temporary matrix with matrix provided by user
    for a2 in range(1,row2+1):  
     for b2 in range(1,column2+1):
        ab2=a2;
        bc2=b2;
        hello2=int(input(f"enter the order a{ab2}{bc2} "))
        outer_List2[ab2-1][bc2-1]=hello2;
    for k2 in range(row2):
     print(outer_List2[k2])                                                                                                      

    # code for addition of matrix
    #creating temporary added matrix
    question=input("Do you want to add the matrix?(y/n)")
    added_matrix=[]
    ilist3=[]
    for i3 in range(row):
        ilist3=[]
        for j3 in range(column):
            ilist3.append("+")
        added_matrix.append(ilist3)

    #adding the matrix and replacing temporary matrix
    if question=="Y" or question=="y":
        if row==row2 and column==column2:
            for g in range(1,row+1):
                for h in range(1,column+1):
                    gh=g;
                    hi=h;
                    added_matrix[gh-1][hi-1]= outer_List[gh-1][hi-1]+outer_List2[gh-1][hi-1]
            for k3 in range(row):                                                                                               
             print(added_matrix[k3])
        else:
            print("The Order of matrix one and matrix 2 needs to be same")
    else:
     print("Thank you")
add_matrix()
