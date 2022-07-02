import math
import random


def creat_points(nums):
    res =[]
    for i in range(nums):
        res.append([random.randint(0,1000),random.randint(0,1000)])
    return res

def k_startpoins(res,num):
    res0=[]
    for i in range(1,num+1):
        res0.append(res[int(len(res)/(num+1)*(i))])
    return res0

def dis(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

def chosepoints(a,res0):
    l=[]
    for i in range(res0):
        l.append(dis(a,res0[i]))
    return l.index(min(l))

def change(res):
    res0=[]
    for i in range(len(res)):
        sumx=0
        sumy=0
        for j in range(len(res[i])):
            sumx=res[i][j][0]+sumx
            sumy=res[i][j][1]+sumy
        x=int(sumx/len(res[i]))
        y=int(sumy/len(res[i]))
        res0.append([x,y])
    return res0
print(change([creat_points(100),creat_points(100)]))

