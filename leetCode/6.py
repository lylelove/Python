

def q6(s,numRows):
    res0=[]
    for i in range(len(s)):
        res0.append([0])
        for j in range(len(s)):
            res0[i].append(0)
    return res0

    

print(q6("PAYPALISHIRING",3))