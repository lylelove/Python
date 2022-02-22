def isa(s,t):
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        if s.count(s[i])!=t.count(s[i]):
            return False
    return True
print(isa("anamule","elumana"))