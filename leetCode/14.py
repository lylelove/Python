def q14():
    strs = ["ab","ab","abcdf"]
    s = ""
    min0=0
    for i in range(len(strs)):
        if len(strs[min0])>len(strs[i]):
            min0 = i
    if len(strs[min0])==0:
        return s
    for i in range(len(strs[min0])):
        allin = True
        for j in range(0, len(strs)):
            temp1 = str(strs[min0][i])
            temp2 = str(strs[j][i])
            if temp1 != temp2:
                allin = False
        if allin:
            s=s+str(strs[min0][i])
        else:
            break
    return (s)
print(q14())
