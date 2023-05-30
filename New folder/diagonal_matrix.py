def is_diagonal(matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix)):
        if i != j and matrix[i][j] != 0:
          return False
    return True
def list(row, column):
    matrix = []
    ilist = []
    for i in range(1, row+1):
        ilist = []
        for j in range(1, column+1):
            ilist.append(1)
        matrix.append(ilist)
    return matrix
row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

matrix = list(row, column)
for k in range(1, row+1):
    for l in range(1, column+1):
        ask = int(input(f"Enter the value for a{k}{l}: "))
        matrix[k-1][l-1] = ask
for m in range(row):
    print(matrix[m])
if is_diagonal(matrix):
    print("matrix is a diagonal matrix")
else:
    print(" matrix is not a diagonal matrix")