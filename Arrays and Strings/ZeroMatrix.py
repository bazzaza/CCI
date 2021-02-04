import copy

def ZeroMatrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    row_set = set()
    col_set = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in row_set or j in col_set:
                matrix[i][j] = 0







matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#matrix = [[1,1,1],[1,0,1],[1,1,1]]

print("Before:")
for row in matrix:
    print(row)
result = ZeroMatrix(matrix)

print("After:")
for row in matrix:
    print(row)