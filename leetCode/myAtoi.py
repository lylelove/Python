def mya(s):
    if s=="":
        return 0
    if s==" ":
        return 0
    if s=="+":
        return 0
    if s=="-":
        return 0
    if s==".":
        return 0
    a=""
    for i in range(len(s)):
        if s[i].isspace():
            a=a
        else:
            a=a+s[i]
    s=""
    if a[0].isnumeric()==False:
        if a[0]!="-" and a[0]!="+":
            return 0
        else:
            if a[1].isnumeric()==False:
                return 0
    for i in range(len(a)):
        if a[i].isnumeric():
            s=s+a[i]
        else:
            if a[0]!="-" and a[0]!="+":
                break
    s = int(s)
    if a[0]=="-":
        s =-s
    if s>2147483647:
        s = 2147483647
    if s<-2147483648:
        s=-2147483648

    return s

print(mya(" "))