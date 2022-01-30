
hui = True
x =-12321
x=str(x)
while x!='' :
    if x[0]==x[len(x)-1]:
        x = x[1:len(x) - 1]
    else:
        hui=False
        break
print(hui)
