def q1020(grid):
    lu=[]
    res=0
    for i in range(len(grid)):
        if grid[i][0]==1:
            grid[i][0]=-1
            lu.append((i,0))
        if grid[i][len(grid[0])-1]==1:
            grid[i][len(grid[0]) - 1]=-1
            lu.append((i,len(grid[0])-1))
    for i in range(len(grid[0])):
        if grid[0][i]==1:
            grid[0][i]=-1
            lu.append((0,i))
        if grid[len(grid)-1][i]==1:
            grid[len(grid) - 1][i]=-1
            lu.append((len(grid)-1,i))
    for i0 in range(2*len(grid)):
        for i in range(len(lu)):
            if lu[i][0]-1>=0 and grid[lu[i][0]-1][lu[i][1]]==1:
                grid[lu[i][0] - 1][lu[i][1]]=-1
                lu.append((lu[i][0]-1,lu[i][1]))
            if lu[i][0]+1<len(grid) and grid[lu[i][0]+1][lu[i][1]]==1:
                grid[lu[i][0] + 1][lu[i][1]] = -1
                lu.append((lu[i][0] + 1, lu[i][1]))
            if lu[i][1]-1>=0 and grid[lu[i][0]][lu[i][1]-1]==1:
                grid[lu[i][0]][lu[i][1]-1]=-1
                lu.append((lu[i][0],lu[i][1]-1))
            if lu[i][1]+1<len(grid[0]) and grid[lu[i][0]][lu[i][1]+1]==1:
                grid[lu[i][0]][lu[i][1]+1]=-1
                lu.append((lu[i][0],lu[i][1]+1))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                res=res+1
    return res
print(q1020(  [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]))