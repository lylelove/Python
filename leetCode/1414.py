def q1414(k):
    shu=[]
    i=0
    def zu(k):
        shu=[]
        a=0
        b=1
        while a<k:
            a = a+b
            b=a+b
            shu.append(a)
            shu.append(b)
        return shu
    while k!=0:
        shu = zu(k)
        for j in range(len(shu)):
            if shu[len(shu)-1-j]<=k:
                k=k-shu[len(shu)-1-j]
                i=i+1

    return i

print(q1414(99999999))