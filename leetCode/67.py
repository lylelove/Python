def q67(a,b):
    a = int(a,2)
    b = int(b,2)
    c=a+b
    c= bin(c)
    c = c[2:]
    return c
print(q67("11","1"))