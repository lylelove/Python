import math
import random
import numpy as np
from matplotlib import pyplot as plt


# 计算a，b两点间的距离
def dis(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


# 创建nums个随机点
def cre_points(nums):
    res = []
    res0 = []
    for i in range(nums):
        res0.append([random.randint(-200, 200), random.randint(-200, 200)])
    res.append(res0)
    res.append([])
    for i in range(len(res0)):
        res[1].append(int(random.randint(1, 5)))
    return res


# 检查车辆是否超载
def check_load(routes, points):
    sum_load = []
    for i in range(len(routes)):
        sum_load.append(0)
        for j in range(len(routes[i])):
            sum_load[i] = sum_load[i] + points[1][points[0].index(routes[i][j])]
    over_load = False
    for i in range(len(sum_load)):
        if sum_load[i] > 12:
            over_load = True
    return over_load


# 计算一个解决方案的总长度
def sum_dis(routes, points):
    s = 0
    for i in range(len(routes)):
        if len(routes[i]) > 0:
            s = s + dis(routes[i][0], [0, 0])
            for j in range(len(routes[i]) - 1):
                s = s + dis(routes[i][j], routes[i][j + 1])
            s = s + dis([0, 0], routes[i][len(routes[i]) - 1])
    if check_load(routes, points):
        s = float('inf')
    return s


# 随机变换路径中的顺序
def change_res(routes, points):
    routes_changed = []
    for i in range(len(routes)):
        routes_changed.append([])
        for j in range(len(routes[i])):
            routes_changed[i].append(routes[i][j])
    c = random.randint(0, 4)
    if c == 0:
        if len(routes_changed) > 1:
            xi = random.randint(0, len(routes_changed) - 1)
            for j in range(len(routes_changed[xi])):
                yi = random.randint(0, len(routes_changed) - 1)
                while yi == xi:
                    yi = random.randint(0, len(routes_changed) - 1)
                routes_changed[yi].append(routes_changed[xi].pop())
    if c == 1:
        xi = random.randint(0, len(routes_changed) - 1)
        yi = random.randint(0, len(routes_changed) - 1)
        if len(routes_changed[xi]) >= 1:
            if len(routes_changed[yi]) >= 1:
                xj = random.randint(0, len(routes_changed[xi]) - 1)
                yj = random.randint(0, len(routes_changed[yi]) - 1)
                temp = []
                for j in range(len(routes_changed[xi][xj])):
                    temp.append(routes_changed[xi][xj][j])
                routes_changed[xi][xj] = []
                for j in range(len(routes_changed[yi][yj])):
                    routes_changed[xi][xj].append(routes_changed[yi][yj][j])
                routes_changed[yi][yj] = []
                for j in range(len(temp)):
                    routes_changed[yi][yj].append(temp[j])
    if c == 2:
        xi = random.randint(0, len(routes_changed) - 1)
        while len(routes_changed[xi]) < 2:
            xi = random.randint(0, len(routes_changed) - 1)
        routes_changed.append([routes_changed[xi].pop()])
    if c > 2:
        xi = random.randint(0, len(routes_changed) - 1)
        yi = random.randint(0, len(routes_changed) - 1)
        while len(routes_changed[xi]) < 2:
            xi = random.randint(0, len(routes_changed) - 1)
        routes_changed[yi].append(routes_changed[xi].pop())
    return routes_changed


# 计算种群中所有路径中的最短路径
def kl_min(kl, routes, points):
    all_routes = []
    all_dis = []

    for i in range(kl):
        routes_changed = change_res(routes, points)
        all_routes.append(routes_changed)
        all_dis.append(sum_dis(routes_changed, points))
    return min(all_dis), all_routes[all_dis.index(min(all_dis))]


# 计数（非主要）
def jishu(T0, r, Ts):
    num = 0
    T = T0
    while T > Ts:
        num = num + 1
        T = T * r
    return num


# 初始解
def initial_solution(points):
    routes = []
    routes_load = 0
    temp = []
    for i in range(len(points[0])):
        routes_load = routes_load + points[1][i]
        if routes_load <= 10:
            temp.append(points[0][i])
        else:
            routes_load = points[1][i]
            routes.append(temp)
            temp = []
            temp.append(points[0][i])
    return routes


# 主方法
def sa(points):
    T0 = 3000
    r = 0.98
    Ts = 0.01
    kl = 500
    T = T0
    routes = initial_solution(points)
    temp_min = sum_dis(routes, points)
    num = jishu(T0, r, Ts)
    num1 = 0
    min_list = []
    while T > Ts:
        # 计数
        for i in range(100):
            if num1 == (i + 1) * int(num / 100):
                print(str(i + 1) + "%")
        num1 = num1 + 1
        #
        T = T * r
        a = kl_min(kl, routes, points)
        if a[0] <= temp_min:
            routes = a[1]
            temp_min = a[0]
        else:
            df = a[0] - temp_min
            p = math.exp(-df / T)
            if random.randint(1, 100) / 100 <= p:
                routes = a[1]
                temp_min = a[0]
        min_list.append(temp_min)
    return routes, min_list


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


def draw_last(routes):
    plt.figure()
    routes_draw_xi = []
    routes_draw_yi = []
    for i in range(len(routes)):
        routes_draw_xi.append([])
        routes_draw_yi.append([])
        routes_draw_xi[i].append(0)
        routes_draw_yi[i].append(0)
        for j in range(len(routes[i])):
            routes_draw_xi[i].append(routes[i][j][0])
            routes_draw_yi[i].append(routes[i][j][1])
        routes_draw_xi[i].append(0)
        routes_draw_yi[i].append(0)
    for i in range(len(routes_draw_xi)):
        x = np.array(routes_draw_xi[i])
        y = np.array(routes_draw_yi[i])
        plt.plot(x, y, marker='o')
    plt.show()
    return routes_draw_xi, routes_draw_yi


points = cre_points(30)
a = sa(points)
plot(a[1])
draw_last(a[0])
print(a[1][len(a[1]) - 1])
