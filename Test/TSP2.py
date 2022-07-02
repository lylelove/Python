import math

res = [[10, -201], [-117, -68], [-126, -263], [-293, 135], [117, -168], [-145, -12], [-193, -279], [96, -236], [98, -232], [131, -148], [81, -217], [-94, -210], [-148, -84], [-245, 99], [77, 129], [-80, 89], [-295, -153], [7, -277], [131, -209], [165, 183], [32, -19], [-17, 47], [5, 181], [-84, -229], [-196, -67], [250, 63], [-255, -138], [-95, 108], [6, -269], [195, 191]]
def dis(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))
def alldis(res):
    disall=[]
    for i in range(len(res)):
        disall.append([-1])
    for i in range(len(res)):
        for j in range(len(res)):
            disall[i].append(dis(res[i],res[j]))
    for i in range(len(disall)):
        disall[i].pop(0)
    return disall

def fun_min(res0):
    min=0
    while res0:
        res0[min]
print(alldis(res))
