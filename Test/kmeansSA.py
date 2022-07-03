import math
import random
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def lens(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def create_points(num):
    total_all = []
    temp_all = []
    temp_all_customer = []
    temp_part_customer = []
    for i in range(num):
        xi = random.randint(0, 200)
        yi = random.randint(0, 200)
        while [xi, yi] in temp_all:
            xi = random.randint(0, 200)
            yi = random.randint(0, 200)
        temp_all.append([xi, yi])
    for i in range(len(temp_all)):
        temp_part_customer = []
        for j in range(random.randint(2, 4)):
            xi = temp_all[i][0] + random.randint(-30, 30)
            yi = temp_all[i][1] + random.randint(-30, 30)
            while [xi, yi] in temp_all_customer:
                xi = temp_all[i][0] + random.randint(-30, 30)
                yi = temp_all[i][1] + random.randint(-30, 30)
            temp_part_customer.append([xi, yi])
            temp_all_customer.append([xi, yi])
        total_all.append([temp_all[i], temp_part_customer])
    return total_all


def separate_points(total_all):
    sender = []
    customer = []
    customer_affiliation = []
    for i in range(len(total_all)):
        sender.append(total_all[i][0])
        for j in range(len(total_all[i][1])):
            customer.append(total_all[i][1][j])
            customer_affiliation.append(i)
    return sender, customer, customer_affiliation


def k_means(customer):
    X = np.array(customer)
    kmeans = KMeans(n_clusters=18, random_state=0).fit(X)
    customer_aaffiliation = kmeans.labels_.tolist()
    c_points = kmeans.cluster_centers_.tolist()
    return customer_aaffiliation, c_points


def change_sender(old_sender, new_sender, customer):
    tolerance = 0.8
    o_s_c_dis = lens(old_sender, customer) * tolerance
    n_s_c_dis = lens(new_sender, customer)
    if n_s_c_dis <= o_s_c_dis:
        return True
    else:
        return False


def draw_first(total_all):
    plt.figure()
    xi = []
    yi = []
    for i in range(len(total_all)):
        xi = []
        yi = []
        xi.append(total_all[i][0][0])
        yi.append(total_all[i][0][1])
        plt.scatter(total_all[i][0][0], total_all[i][0][1])
        for j in range(len(total_all[i][1])):
            plt.scatter(total_all[i][1][j][0], total_all[i][1][j][1])
            xi.append(total_all[i][1][j][0])
            yi.append(total_all[i][1][j][1])
            xi.append(total_all[i][0][0])
            yi.append(total_all[i][0][1])
        x = np.array(xi)
        y = np.array(yi)
        plt.plot(x, y)
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


# 计算a，b两点间的距离
def dis(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


# 检查车辆是否超载
def check_load(routes, points):
    sum_load = []
    for i in range(len(routes)):
        sum_load.append(0)
        for j in range(len(routes[i])):
            sum_load[i] = sum_load[i] + points[1][points[0].index(routes[i][j])]
    over_load = False
    for i in range(len(sum_load)):
        if sum_load[i] > 20:
            over_load = True
    return over_load


# 计算一个解决方案的总长度
def sum_dis(routes, points):
    s = 0
    for i in range(len(routes)):
        s = s + 50
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
        if routes_load <= 20:
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
    r = 0.96
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


def sum_s_c_dis(customer_affiliation, customer, sender):
    sum_dis = 0
    for i in range(len(customer)):
        sum_dis = sum_dis + dis(customer[i], sender[customer_affiliation[i]])
    return sum_dis


if __name__ == '__main__':
    total_points = create_points(30)
    draw_first(total_points)
    sender, customer, customer_affiliation = separate_points(total_points)
    old_sum_dis = sum_s_c_dis(customer_affiliation, customer, sender)
    new_customer_affiliation, c_points = k_means(customer)
    cp_s_dis = []
    for i in range(len(c_points)):
        temp = []
        for j in range(len(sender)):
            temp.append(lens(c_points[i], sender[j]))
        cp_s_dis.append(temp)
    cp_affiliation = []
    for i in range(len(cp_s_dis)):
        cp_affiliation.append(cp_s_dis[i].index(min(cp_s_dis[i])))
    new_new_customer_affiliation = []
    for i in range(len(new_customer_affiliation)):
        new_new_customer_affiliation.append(cp_affiliation[new_customer_affiliation[i]])
    all_sender = []
    for i in range(len(new_new_customer_affiliation)):
        if all_sender.count(new_new_customer_affiliation[i]) == 0:
            all_sender.append(new_new_customer_affiliation[i])
    for i in range(len(customer_affiliation)):
        if customer_affiliation[i] != new_new_customer_affiliation[i]:
            if change_sender(sender[customer_affiliation[i]], sender[new_new_customer_affiliation[i]], customer[i]):
                customer_affiliation[i] = new_new_customer_affiliation[i]
            else:
                if all_sender.count(customer_affiliation) == 0:
                    customer_affiliation[i] = new_new_customer_affiliation[i]
                else:
                    customer_affiliation[i] = customer_affiliation[i]
    new_sum_dis = sum_s_c_dis(customer_affiliation, customer, sender)
    select_sender = [[], []]
    for i in range(len(all_sender)):
        select_sender[0].append(sender[all_sender[i]])
        select_sender[1].append(0)
    for i in range(len(customer_affiliation)):
        for j in range(len(select_sender[0])):
            if customer_affiliation[i] == all_sender[j]:
                select_sender[1][j] = select_sender[1][j] + 1
    old_select_sender=[[],[]]
    for i in range(len(total_points)):
        old_select_sender[0].append(total_points[i][0])
        old_select_sender[1].append(len(total_points[i][1]))
    new_total_points = []
    for i in range(len(select_sender[0])):
        new_total_points.append([])
        new_total_points[i].append(select_sender[0][i])
        temp = []
        for j in range(len(customer_affiliation)):
            if customer_affiliation[j] == all_sender[i]:
                temp.append(customer[j])
        new_total_points[i].append(temp)
    routes = sa(select_sender)
    # old_routes=sa(old_select_sender)
    draw_first(new_total_points)
    draw_last(routes[0])
    print(routes[1][len(routes[1]) - 1])
