def q884(s1,s2):
    res = []
    s3 = s1.split()
    s4 = s2.split()
    s5 = s1.split()
    s6 = s2.split()
    s7=[]
    s8=[]
    while s3:
        i = s3.pop()
        if i in s3:
            s7.append(i)
            continue
        if i in s7:
            s7.append(i)
            continue
        if i in s5 and i in s6:
            s7.append(i)
            continue
        else:
            s7.append(i)
            res.append(i)
    while s4:
        j = s4.pop()
        if j in s4:
            s8.append(j)
            continue
        if j in s8:
            s8.append(j)
            continue
        if j in s5 and j in s6:
            s8.append(j)
            continue
        else:
            s8.append(j)
            res.append(j)
    return res
print(q884("this apple is sweet"
,"this apple is sour"))
