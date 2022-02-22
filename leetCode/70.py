def q70(n):
    res=1
    for i in range(1,int(n/2)+1):
        s=1
        x=1
        for j in range(1,i+1):
            s=s*(n-i-j+1)
            x = j*x
        a=s/x
        res=res+a
    return int(res)
print(q70(3))