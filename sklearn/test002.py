import random


def nums_out(wi, bi, num):
    res = 0
    for i in range(len(wi)):
        res = res + wi[i] * num + bi[i]
    return res


def change_wb(best_wi, best_bi):
    wi = []
    for i in range(len(best_wi)):
        wi.append(best_wi[i])
    bi = []
    for i in range(len(best_bi)):
        bi.append(best_bi[i])
    for i in range(len(wi)):
        temp = random.randint(0, 2)
        if temp == 0:
            wi[i] = wi[i] - 0.01
        if temp == 1:
            wi[i] = wi[i]
        if temp == 2:
            wi[i] = wi[i] + 0.01
    for i in range(len(bi)):
        temp = random.randint(0, 2)
        if temp == 0:
            bi[i] = bi[i] - 0.01
        if temp == 1:
            bi[i] = bi[i]
        if temp == 2:
            bi[i] = bi[i] + 0.01
    return wi, bi


def search_all(bi, wi, nums, gen, size, ress):
    best_wi = []
    best_lin = []
    for i in range(len(wi)):
        best_wi.append(wi[i])
    best_bi = []
    for i in range(len(bi)):
        best_bi.append(bi[i])
    best_res_dis = 0
    temp_res = 0
    best_ress = []
    for i in range(len(nums)):
        temp_res = nums_out(wi, bi, nums[i])
        best_res_dis = best_res_dis + abs(ress[i] - temp_res)
        best_ress.append(temp_res)
    best_lin.append(best_res_dis)
    for i in range(gen):
        gen_wi = []
        gen_bi = []
        for j in range(size):
            temp_wi, temp_bi = change_wb(best_wi, best_bi)
            gen_wi.append(temp_wi)
            gen_bi.append(temp_bi)
        for j in range(size):
            temp_dis = 0
            for k in range(len(nums)):
                temp_res = nums_out(gen_wi[k], gen_bi[k], nums[k])
                temp_dis = temp_dis + abs(ress[k] - temp_res)
            if best_res_dis > temp_dis:
                best_res_dis = temp_dis
                best_wi = []
                for p in range(len(gen_wi[j])):
                    best_wi.append(gen_wi[j][p])
                best_bi = []
                for p in range(len(gen_bi[j])):
                    best_bi.append(gen_bi[j][p])
                best_ress = []
                for p in range(len(nums)):
                    temp_res = nums_out(best_wi, best_bi, nums[p])
                    best_ress.append(temp_res)
        best_lin.append(best_res_dis)
    return best_res_dis, best_wi, best_bi, best_lin, best_ress


if __name__ == '__main__':
    bi = [1, 1, 1, 1, 1, 1, 1]
    wi = [1, 1, 1, 1, 1, 1, 1]
    gen = 100
    size = 100
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ress = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    a = search_all(bi, wi, nums, gen, size, ress)
    res = nums_out(a[1], a[2], 10)
