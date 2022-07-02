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


def k_means(customer):
    X = np.array(customer)
    kmeans = KMeans(n_clusters=8, random_state=0).fit(X)
    customer_aaffiliation = kmeans.labels_.tolist()
    c_points = kmeans.cluster_centers_.tolist()
    return customer_aaffiliation, c_points


def change_sender(old_sender,new_sender,customer):
    tolerance=0.8
    o_s_c_dis=lens(old_sender,customer)*tolerance
    n_s_c_dis=lens(new_sender,customer)
    if n_s_c_dis<=o_s_c_dis:
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


if __name__ == '__main__':
    sender, customer, customer_affiliation = separate_points(create_points(20))
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
        if all_sender.count(new_new_customer_affiliation[i])==0:
            all_sender.append(new_new_customer_affiliation[i])
    jishu=0
    for i in range(len(customer_affiliation)):
        if customer_affiliation[i]!=new_new_customer_affiliation[i]:
            if change_sender(sender[customer_affiliation[i]],sender[new_new_customer_affiliation[i]],customer[i]):
                customer_affiliation[i]=new_new_customer_affiliation[i]
                jishu=jishu+1
            else:
                if all_sender.count(customer_affiliation) == 0:
                    customer_affiliation[i] = new_new_customer_affiliation[i]
                    jishu = jishu + 1
                else:
                    customer_affiliation[i]=customer_affiliation[i]
                    
