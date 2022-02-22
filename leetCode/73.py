def q73(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(len(matrix[i])):
                    if matrix[i][k]!=0:
                        matrix[i][k] = "z"
                for k in range(len(matrix)):
                    if matrix[k][j]!=0:
                        matrix[k][j] = "z"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "z":
                matrix[i][j] = 0
    return matrix


print(q73([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
