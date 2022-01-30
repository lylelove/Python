import math

word = "zasdfg"
st = 0
p = 0
pan = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(word)):
    print(p)
    for j in range(len(pan)):
        if word[i] == pan[j]:
            if math.fabs(j - st) > 13:
                if st>13:
                    p = p+25-st+j+2
                else:
                    p = p + 25 - j + st + 2
                st = j;
                break
            else:
                p = int(p+math.fabs(j-st)+1)
                st=j
                break
    
print(p)
