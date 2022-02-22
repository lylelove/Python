def q74(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][len(matrix[i]) - 1] >= target:
            return target in matrix[i]
    return False

print(q74([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 10))
