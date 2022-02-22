def q1380(matrix):
    minl = []
    res = []
    for i in range(len(matrix)):
        minl.append(min(matrix[i]))
    for i in range(len(minl)):
        maxr = True
        for j in range(len(matrix)):
            if matrix[j][matrix[i].index(minl[i])] <= minl[i]:
                continue
            else:
                maxr = False
        if maxr:
            res.append(minl[i])
    return res


print(q1380([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
