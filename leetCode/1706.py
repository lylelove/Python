def q1706(grid):
    res = []
    if len(grid[0])==1:
        return grid
    for i in range(len(grid[0])):
        n = i
        for j in range(len(grid)):
            if 0 < n < len(grid[0]) - 1:
                if grid[j][n] == 1 and grid[j][n + 1] == -1:
                    n = -1
                    break
                if grid[j][n] == 1 and grid[j][n + 1] == 1:
                    n = n + 1
                if grid[j][n] == -1 and grid[j][n - 1] == 1:
                    n = -1
                    break
                if grid[j][n] == -1 and grid[j][n - 1] == -1:
                    n = n - 1

            elif n == 0:
                if grid[j][n] == 1 and grid[j][n + 1] == -1:
                    n = -1
                    break
                if grid[j][n] == 1 and grid[j][n + 1] == 1:
                    n = n + 1
                if grid[j][n] == -1:
                    n = -1
                    break
            elif n == len(grid[0]) - 1:
                if grid[j][n] == -1 and grid[j][n - 1] == 1:
                    n = -1
                    break
                if grid[j][n] == -1 and grid[j][n - 1] == -1:
                    n = n - 1
                if grid[j][n] == 1:
                    n = -1
                    break
        res.append(n)
    return res


print(q1706([[1]]))
