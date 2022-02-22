def isp(s):
    s =s.lower()
    l=[]
    for i in range(len(s)):
        if s[i].isalpha() or s[i].isalnum():
            l.append(s[i])
    l1=l.copy()
    l.reverse()
    if l1==l:
        return True
    else:
        return False
print(isp("0P"))