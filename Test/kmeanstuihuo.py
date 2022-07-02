import math
import random
from matplotlib import pyplot as plt
import numpy as np


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
        for j in range(random.randint(3, 8)):
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


a, b, c = separate_points(create_points(20))


def k_means(customer):
    global new_c_points
    global customer_affiliation
    global c_points_customer

    for i in range(int(len(customer) / 5)):
        new_c_points = []
        k=0
        while k<20:
            k=k+1
            all_dis = []
            c_points = []
            customer_affiliation = []
            c_points_customer = []
            for j in range(i):
                if not new_c_points:
                    c_points.append(customer[int(len(customer) / (i + 1) * j)])
                all_dis.append([])
                c_points_customer.append([])
            for j in range(len(customer)):
                temp = []
                for q in range(i):
                    if len(new_c_points) > 0:
                        all_dis[q].append(lens(customer[j], new_c_points[q]))
                    else:
                        all_dis[q].append(lens(customer[j], c_points[q]))
                for w in range(i):
                    temp.append(all_dis[w][j])
                if len(temp) > 0:
                    customer_affiliation.append(temp.index(min(temp)))
            for j in range(len(customer_affiliation)):
                for q in range(i):
                    if customer_affiliation[j] == q:
                        c_points_customer[q].append(customer[j])
            for j in range(len(c_points)):
                xi = 0
                yi = 0
                for q in range(len(c_points_customer[j])):
                    xi = xi + c_points_customer[j][q][0]
                    yi = yi + c_points_customer[j][q][1]
                new_c_points.append([xi / len(c_points_customer[j]), yi / len(c_points_customer[j])])
            print(customer_affiliation)
    return customer_affiliation, c_points_customer, new_c_points


d, e, f = k_means(b)


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
