import copy

def ZeroMatrix(m):

    n = copy.deepcopy(m)


    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                n[i] = [0 for item in n[i]]
                for r in n:
                    r[j] =0

    return n



matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]

result = ZeroMatrix(matrix)
print(result)
print(matrix)