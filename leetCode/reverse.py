def rev(x):
    if x>=2147483647 or x<=-2147483648:
        return 0
    if x>=0:
        s=[]
        x=str(x)
        for i in range(len(x)):
            s.append(x[i])
        s.reverse()
        x=""
        for i in range(len(s)):
            x=x+str(s[i])
        return int(x)
    if x<0:
        x=-x
        s=[]
        x=str(x)
        for i in range(len(x)):
            s.append(x[i])
        s.reverse()
        x=""
        for i in range(len(s)):
            x=x+str(s[i])
        return -int(x)

print(rev(-120))