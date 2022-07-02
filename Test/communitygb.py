import math
import random
import matplotlib.pyplot as plt
import turtle


def gen(num):
    res = []
    for i in range(num):
        a = [random.randint(0, 100), random.randint(0, 100)]
        while a in res:
            a = [random.randint(0, 100), random.randint(0, 100)]
        res.append(a)
    return res


def lens(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def cutpoints(res):
    reslens = []
    res1 = []
    for i in range(len(res)):
        res1.append(res[i])
    for i in range(len(res1)):
        a = 0
        for j in range(len(res1)):
            a = a + int(lens(res1[i], res1[j]))
        reslens.append(a)
    b = reslens.index(min(reslens))
    res1.pop(b)
    return res1


def kmeans(res, customer):
    res1 = []
    res0 = 0
    for i in range(len(res)):
        res1.append([i])
    for i in range(len(customer)):
        res3 = []
        for j in range(len(res)):
            res3.append(lens(customer[i], res[j]))
        res1[res3.index(min(res3))].append(customer[i])
        res0 = res0 + min(res3)
    for i in range(len(res1)):
        res1[i].pop(0)
    return res1, res0


def changek(lists):
    res = []
    for i in range(len(lists)):
        x = 0
        y = 0
        num = 0
        for j in range(len(lists[i])):
            x = x + lists[i][j][0]
            y = y + lists[i][j][1]
            num = num + 1
        if num > 0:
            res.append([int(x / num), int(y / num)])
    return res


def inkmeans(res, customer):
    a = []
    cir = True
    while cir:
        for i in range(3):
            a.append(int(kmeans(res, customer)[1]))
            res = changek(kmeans(res, customer)[0])
        if a[len(a) - 1] == a[len(a) - 2] and a[len(a) - 2] == a[len(a) - 3]:
            cir = False
    return res


def plins(res, lists):
    l = 0
    num = 0
    for i in range(len(res)):
        for j in range(len(lists[i])):
            l = l + lens(res[i], lists[i][j])
            if lens(res[i], lists[i][j]) > 0:
                num = num + 1
    return int(l / num)


def outkmeans(res, customer):
    pl = 0
    num = 0
    linlist = []
    plist = []
    while pl < 12:
        num = num + 1
        res = cutpoints(res)
        res = inkmeans(res, customer)
        lists = kmeans(res, customer)[0]
        linlist.append(kmeans(res, customer)[1])
        pl = plins(res, lists)
        plist.append(pl)
        print(str(num) + "/150")
    return res, linlist, plist


def draw(res, customer):
    lists = kmeans(res, customer)[0]
    turtle.setup()
    turtle.pensize(1)
    turtle.hideturtle()
    turtle.speed(10)
    for i in range(len(res)):
        turtle.penup()
        turtle.goto((res[i][0] - 50) * 6, (res[i][1] - 50) * 4)
        turtle.pendown()
        turtle.dot(7, "red")
    for i in range(len(lists)):
        turtle.penup()
        for j in range(len(lists[i])):
            turtle.goto((lists[i][j][0] - 50) * 6, (lists[i][j][1] - 50) * 4)
            turtle.pendown()
            turtle.dot(4, "black")
            turtle.penup()
    for i in range(len(lists)):
        turtle.penup()
        for j in range(len(lists[i])):
            turtle.goto((res[i][0] - 50) * 6, (res[i][1] - 50) * 4)
            turtle.pendown()
            turtle.goto((lists[i][j][0] - 50) * 6, (lists[i][j][1] - 50) * 4)
            turtle.penup()


def drawsa(res):
    turtle.goto(-300, -200)
    turtle.dot(10, "red")
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("blue")
    for i in range(len(res)):
        turtle.goto((res[i][0] - 50) * 6, (res[i][1] - 50) * 4)
    turtle.goto(-300, -200)
    turtle.mainloop()


def plot(linlist):
    y = []
    for i in range(len(linlist)):
        y.append(i)
    plt.plot(y, linlist, label='linear')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()
    plt.show()


def sa(res):
    global suml
    T0 = 3000
    r = 0.998
    Ts = 0.01
    lk = 300
    T = T0
    suma = 0
    num = 0
    mingen = []
    start = [0, 0]
    for i in range(len(res) - 1):
        suma = suma + lens(res[i], res[i + 1])
    suma = suma + lens(res[0], start) + lens(res[len(res) - 1], start)
    mingen.append(suma)
    while T > Ts:
        num = num + 1
        print(str(num) + "/625")
        sunlist = []
        sumindex = []
        for i in range(lk):
            r1 = random.randint(0, len(res) - 1)
            r2 = random.randint(0, len(res) - 1)
            while r1 == r2:
                r2 = random.randint(0, len(res) - 1)
            temp = res[r1]
            res[r1] = res[r2]
            res[r2] = temp
            sunl = 0
            for j in range(len(res) - 1):
                sunl = sunl + lens(res[j], res[j + 1])
            sunl = sunl + lens(res[0], start) + lens(res[len(res) - 1], start)
            sunlist.append(sunl)
            sumindex.append([r1, r2])
            res[r2] = res[r1]
            res[r1] = temp
        if min(sunlist) < suma:
            suma = min(sunlist)
            mingen.append(min(sunlist))
            temp = res[sumindex[sunlist.index(min(sunlist))][0]]
            res[sumindex[sunlist.index(min(sunlist))][0]] = res[sumindex[sunlist.index(min(sunlist))][1]]
            res[sumindex[sunlist.index(min(sunlist))][1]] = temp
        else:
            df = min(sunlist) - suma
            p = math.exp(-df / T)
            if random.randint(1, 10) / 10 <= p:
                mingen.append(min(sunlist))
                temp = res[sumindex[sunlist.index(min(sunlist))][0]]
                res[sumindex[sunlist.index(min(sunlist))][0]] = res[sumindex[sunlist.index(min(sunlist))][1]]
                res[sumindex[sunlist.index(min(sunlist))][1]] = temp
            else:
                mingen.append(min(sunlist))
        T = T * r
    return res, mingen


a = [[150, 187], [67, 25], [68, 64], [185, 168], [112, 115], [135, 160], [140, 98], [129, 48], [35, 67], [80, 172], [92, 42], [193, 1], [98, 176], [1, 184], [30, 118], [79, 39], [8, 175], [190, 91], [74, 114], [189, 7]]
res1=outkmeans(a,a)

draw(res1[0],a)

