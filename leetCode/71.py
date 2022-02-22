def q71(path):
    o = path.split("/")
    o1=[]
    s=""
    for i in range(len(o)):
        if len(o[i])>0:
            o1.append(o[i])
    o=[]
    for i in range(len(o1)):
        if o1[i]==".":
            continue
        if o1[i]=="..":
            if len(o)>=1:
                o.pop()
            continue
        o.append(o1[i])
        s=""
    for i in range(len(o)):
        s=s+"/"+o[i]
    if s=="":
        s="/"
    return s
print(q71("/.."))