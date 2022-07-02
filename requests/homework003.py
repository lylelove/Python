import math
import re
import turtle
import matplotlib.pyplot as plt


def loadDataSet():
    dataSet = []
    with open('kmeans.txt') as fp:
        for line in fp.readlines():
            curline = re.split('\s+', line.strip())
            fltline = list(map(float, curline))
            dataSet.append(fltline)
    return dataSet


def dot_draw(e):
    turtle.setup()
    turtle.hideturtle()
    turtle.speed(10)
    for k in range(len(e[2])):
        for x,y in e[2][k]:
            turtle.penup()
            turtle.goto(50 * x, 50 * y)
            turtle.pendown()
            turtle.dot(5, "blue")
    for i in range(len(e[1])):
        x1,y1 = e[1][i]
        turtle.penup()
        turtle.goto(50*x1,50*y1)
        turtle.pendown()
        turtle.dot(8,'black')
        for x,y in e[2][i]:
            turtle.goto(50*x,50*y)
            turtle.penup()
            turtle.goto(50*x1,50*y1)
            turtle.pendown()
    turtle.mainloop()


def dis(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def classify(c_points, s_points):
    res = []
    for i in range(len(s_points)):
        res.append([])
    for point in c_points:
        temp = []
        for s_point in s_points:
            temp.append(dis(point, s_point))
        res[temp.index(min(temp))].append(point)
    return res


def interation(classify_list):
    res = []
    for i in range(len(classify_list)):
        res.append([])
    for i in range(len(classify_list)):
        sum_x = 0
        sum_y = 0
        for point in classify_list[i]:
            sum_x = sum_x + point[0]
            sum_y = sum_y + point[1]
        res[i].append(sum_x / len(classify_list[i]))
        res[i].append(sum_y / len(classify_list[i]))
    return res


def sumdis(c, s):
    sum = []
    for i in range(len(s)):
        temp = 0
        for point in c[i]:
            temp = temp + dis(s[i], point)
        sum.append(temp)
    return sum


def Elbow(c, s):
    sum = 0
    for i in range(len(s)):
        for k in c[i]:
            sum = sum + math.pow(dis(s[i], k), 2)
    return sum


def cutpoint(sumdis, s):
    res = []
    for i in s:
        res.append(i)
    res.pop(sumdis.index(min(sumdis)))
    return res


def kmeans(c, s):
    for i in range(20):
        b = classify(c, s)
        s = interation(b)
        b = classify(c, s)
    return c, s, b


def main(num):
    c = loadDataSet()
    s = []
    res = []
    num=int(num)
    for i in c:
        s.append(i)
    while len(s) > num:
        b = classify(c, s)
        sum = sumdis(b, s)
        res.append(Elbow(b, s))
        s = cutpoint(sum, s)
        e = kmeans(c, s)
    if num==1:
        return res
    else:
        return e

def plot(linlist):
    linlist.reverse()
    y = []
    for i in range(len(linlist)):
        y.append(i)
    plt.plot(y, linlist, label='linear')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

a = main(1)
plot(a)
e =main(input('K:'))
dot_draw(e)

