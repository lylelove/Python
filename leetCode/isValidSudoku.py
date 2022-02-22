def isVa(board):
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[i][j]!=".":
                row.append(board[i][j])
        for j in range(len(row)):
            if row.count(row[j])>1:
                return False
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[j][i]!=".":
                row.append(board[j][i])
        for j in range(len(row)):
            if row.count(row[j])>1:
                return False
    for i in [[0,1,2],[3,4,5],[6,7,8]]:
        for j in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            row =[]
            for i1 in i:
                for j1 in j:
                    if board[i1][j1]!=".":
                        row.append(board[i1][j1])
            for j in range(len(row)):
                if row.count(row[j])>1:
                    return False
    return True


print(isVa([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
