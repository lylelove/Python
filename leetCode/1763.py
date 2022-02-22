def q1763(s):
    res=""
    l = "abcdefghigklmnopqrstuvwxyz"
    for i in range(len(s)):
        if l.find(s[i]):
            return s[i]

print(q1763("YazzaAay"))