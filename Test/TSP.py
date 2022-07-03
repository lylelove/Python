import math
import random
import turtle
from matplotlib import pyplot as plt


# 计算a，b两点间的距离
def dis(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


# 创建nums个随机点
def cre_points(nums):
    res = []
    for i in range(nums):
        res.append([random.randint(-300, 300), random.randint(-300, 300)])
    return res


# 计算一条路径的总长度
def sum_dis(res):
    s = 0
    for i in range(len(res) - 1):
        s = s + dis(res[i], res[i + 1])
    s = s + dis(res[0], res[len(res) - 1])
    return s


# 随机变换路径中的顺序
def change_res(res0):
    res = []
    for i in range(len(res0)):
        res.append(res0[i])
    num = int(len(res) / 5)
    if num < 2:
        num = 2
    r = []
    for i in range(num):
        r0 = random.randint(0, len(res) - 1)
        while r0 in r:
            r0 = random.randint(0, len(res) - 1)
        r.append(r0)
    for i in range(len(r)):
        r0 = random.randint(0, len(r) - 1)
        temp = res[r[i]]
        res[r[i]]=res[r[r0]]
        res[r[r0]]=temp
    return res

# 计算种群中所有路径中的最短路径
def kl_min(kl, res):
    all_res = []
    all_dis = []
    for i in range(kl):
        a = change_res(res)
        all_res.append(a)
        all_dis.append(sum_dis(a))
    return min(all_dis), all_res[all_dis.index(min(all_dis))]

# 计数（非主要）
def jishu(T0, r, Ts):
    num = 0
    T = T0
    while T > Ts:
        num = num + 1
        T = T * r
    return num

# 主方法
def sa(res):
    T0 = 3000
    r = 0.995
    Ts = 0.01
    kl = 500
    T = T0
    temp_min = sum_dis(res)
    num = jishu(T0, r, Ts)
    num1 = 0
    min_list = []
    while T > Ts:
        # 计数
        for i in range(100):
            if num1==(i+1)*int(num/100):
                print(str(i+1)+"%")
        num1 = num1 + 1
        #
        T = T * r
        a = kl_min(kl, res)
        if a[0] <= temp_min:
            res = a[1]
            temp_min = a[0]
        else:
            df = a[0] - temp_min
            p = math.exp(-df / T)
            if random.randint(1, 100) / 100 <= p:
                res = a[1]
                temp_min = a[0]
        min_list.append(temp_min)
    return res, min_list

# 迭代图表
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

# 画图
def draw(res):
    turtle.setup()
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(res[0][0], res[0][1])
    turtle.pendown()
    for i in range(len(res)):
        turtle.goto(res[i][0], res[i][1])
        turtle.dot(5, "blue")
    turtle.goto(res[0][0], res[0][1])
    turtle.mainloop()


res = [[73, 187], [80, 39], [185, 34], [195, 42], [70, 181], [30, 80], [40, 177], [24, 79], [177, 72], [79, 124], [85, 12], [199, 128], [23, 125], [134, 5], [193, 118], [40, 103], [19, 39], [152, 186], [125, 148], [143, 36]]
a = sa(res)
plot(a[1])
print(a[1][len(a[1])-1])
print(res)


