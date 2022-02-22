s = input().split()
b1 = int(s[0])
b2 = int(s[1])
m1 = int(s[2])
m2 = int(s[3])
a1 = 0
a2 = 0
m = [[m2, m1]]
walk_over = False
turn = 'd'
line = 0
if m2 - 2 >= 0 and m1 - 1 >= 0:
    m.append([m2 - 2, m1 - 1])
if m2 + 2 <= 20 and m1 - 1 >= 0:
    m.append([m2 + 2, m1 - 1])
if m2 - 1 >= 0 and m1 - 2 >= 0:
    m.append([m2 - 1, m1 - 2])
if m2 + 1 <= 20 and m1 - 2 >= 0:
    m.append([m2 + 1, m1 - 2])
if m2 - 2 >= 0 and m1 + 1 <= 20:
    m.append([m2 - 2, m1 + 1])
if m2 - 1 >= 0 and m1 + 2 <= 20:
    m.append([m2 - 1, m1 + 2])
if m2 + 1 <= 20 and m1 + 2 <= 20:
    m.append([m2 + 1, m1 + 2])
if m2 + 2 <= 20 and m1 + 1 <= 20:
    m.append([m2 + 2, m1 + 1])


def r_walk(i1, i2):
    right = True
    i1 = i1 + 1
    if i1 > b1:
        right = False
    for i in range(len(m)):
        if i2 == m[i][0] and i1 == m[i][1]:
            right = False
    return right


def d_walk(i1, i2):
    down = True
    i2 = i2 + 1
    if i2 > b2:
        down = False
    for i in range(len(m)):
        if i2 == m[i][0] and i1 == m[i][1]:
            down = False
    return down


def al_come(i1, i2):
    alcome = False
    if i1 == b1 and i2 == b2:
        alcome = True
    return alcome


def walk(i1, i2):
    if d_walk(i1, i2):
        i1 = 0
        i2 = 1
    if not d_walk(i1, i2):
        if r_walk(i1, i2):
            i1 = 1
            i2 = 0
    return i1, i2


def inline(i1, i2):
    x =i1
    y=i2
    while not al_come(x, y):
        if walk(x, y)[0] == 0 and walk(x, y)[1] == 0:
            if x == 0 and y == 0:
                print("No Way")
                break
            x = x - temp[0]
            y = y - temp[1]
            continue
        temp = walk(x, y)
        x = x + temp[0]
        y = y + temp[1]
        print(x,y )


inline(0, 0)
