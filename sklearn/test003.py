import math
import random

import numpy as np
from matplotlib import pyplot as plt


def nums_out(train_x, train_y, wi):
    test_y = []
    for i in range(len(train_x)):
        temp_y = 0
        for j in range(len(wi)):
            temp_y = temp_y + wi[j] * math.pow(train_x[i], j)
        test_y.append(temp_y)
    test_y_dis = 0
    for i in range(len(test_y)):
        test_y_dis = test_y_dis + math.pow(abs(test_y[i] - train_y[i]),2)
    return test_y_dis


def test_num(wi, test_x):
    test_y = 0
    for i in range(len(wi)):
        test_y = test_y + wi[i] * pow(test_x,i)
    return test_y


def change_wb(old_wi):
    new_wi = []
    for i in range(len(old_wi)):
        new_wi.append(old_wi[i])
    for i in range(len(new_wi)):
        new_wi[i] = new_wi[i] - 0.1 * random.randint(-200, 200)
    return new_wi


def get_best(best_wi, size, train_x, train_y):
    dis_all = []
    wi_all = []
    for i in range(size):
        new_wi= change_wb(best_wi)
        wi_all.append(new_wi)
        dis_all.append(nums_out(train_x, train_y, new_wi))
    dis_min = dis_all.index(min(dis_all))
    return wi_all[dis_min], dis_all[dis_min]


def gen(wi, num, size, train_x, train_y):
    best_dis = nums_out(train_x, train_y, wi)
    best_dis_lin = [best_dis]
    for i in range(num):
        gen_res = get_best(wi, size, train_x, train_y)
        if gen_res[1] <= best_dis:
            best_dis = gen_res[1]
            wi = gen_res[0]
        best_dis_lin.append(best_dis)
    test_ys = []
    for i in range(len(train_x)):
        test_ys.append(test_num(wi,train_x[i]))
    return best_dis, wi,test_ys, best_dis_lin


def draw_lin(lin):
    ypoints = np.array(lin)
    plt.plot(ypoints)
    plt.show()


if __name__ == '__main__':
    train_x = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
    train_y = [70078, 65534, 59592, 53783, 49922, 46912, 43397, 39771, 36277, 30808]
    wi = [1, 1,1,1,1,1]
    num = 400
    size = 400
    res = gen(wi,num, size, train_x, train_y)
    test_x = [2020,2021]
    test_ys = []
    for i in range(len(test_x)):
        test_ys.append(test_num(res[1], test_x[i]))
    draw_lin(res[3])
