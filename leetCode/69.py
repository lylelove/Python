def q69(x):
    if x == 1:
        return 1
    if x==2:
        return 1
    if x==3:
        return 1
    if x ==4:
        return 2
    if x==5:
        return 2
    if x==6:
        return 2
    if x==7:
        return 2
    if x==8:
        return 2
    if x==9:
        return 3
    for i in range(int(x/2)):
        if i*i>x:
            return i-1
print(q69(25))