from collections import deque


def q1765(isWater):
    m, n = len(isWater), len(isWater[0])
    ans = [[0] * n for i in range(m)]
    d = deque()
    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                d.append((i, j))
            ans[i][j] = 0 if isWater[i][j] else -1
    while len(d):
        i,j=d.popleft()
        tnextin = True
        lnextin = True
        dnextin = True
        rnextin = True
        if i - 1 < 0 or ans[i - 1][j] != -1:
            tnextin = False
        if j - 1 < 0 or ans[i][j - 1] != -1:
            lnextin = False
        if i + 1 >= len(isWater) or ans[i + 1][j] != -1:
            dnextin = False
        if j + 1 >= len(isWater[0]) or ans[i][j + 1] != -1:
            rnextin = False
        if tnextin:
            d.append((i - 1, j))
            ans[i - 1][j] = ans[i][j] + 1
        if lnextin:
            d.append((i, j - 1))
            ans[i][j-1] = ans[i][j] + 1
        if dnextin:
            d.append((i + 1, j))
            ans[i + 1][j] = ans[i][j] + 1
        if rnextin:
            d.append((i, j + 1))
            ans[i][j+1] = ans[i][j] + 1
    return ans


print(q1765([[0,0,1],[1,0,0],[0,0,0]]))
