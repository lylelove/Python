def roimg(matrix):
    for i in range(len(matrix) - 2):
        for j in range(len(matrix) - 1):
            if j%2 !=0 :
                temp1 = matrix[j][len(matrix) - 1 - i]
                temp2 = matrix[i][j]
                temp3 = matrix[len(matrix) - 1 - j][i]
                temp4 = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
                matrix[j][len(matrix) - 1 - i] = temp2
                matrix[i][j] = temp3
                matrix[len(matrix) - 1 - j][i] = temp4
                matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = temp1
            # if j%2==0 :
            #     temp1 = matrix[j][i]
            #     temp2 = matrix[len(matrix) - 1 - i][j]
            #     temp3 = matrix[len(matrix) - 1 - j][len(matrix) - 1 - i]
            #     temp4 = matrix[i][len(matrix) - 1 - j]
            #     matrix[j][i] = temp2
            #     matrix[len(matrix) - 1 - i][j] = temp3
            #     matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] = temp4
            #     matrix[i][len(matrix) - 1 - j] = temp1
    return matrix


print(roimg(
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
