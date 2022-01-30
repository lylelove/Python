a = "q-,  "
number = "1234567890"
ch = "abcdefghijklmnopqrstuvwxyz"
fuhao = "!.,"
strover = False
num = 0
s = []
while not strover:
    po = a.find(" ")
    if po == 0:
        a = a[1:len(a)]
        continue
    if po == -1:
        s.append(a)
        strover = True
        continue
    s.append(a[0:po])
    a = a[po:]
for i in range(len(s)):
    for j in range(len(number)):
        if s[i].find(number[j]) != -1:
            s[i] = "1"

for i in range(len(s)):
    if len(s[i]) > 1:
        ch0 = False
        for j in range(len(ch)):
            if s[i][0] == ch[j]:
                ch0 = True
                break
        if not ch0:
            s[i] = "2"

for i in range(len(s)):
    if s[i].find("-") != -1:
        temp = s[i][s[i].find("-") + 1:]
        if temp.find("-") != -1:
            s[i] = "3"
            continue
    if s[i].find("-") == len(s[i]) - 1:
        s[i] = "3"
for i in range(len(s)):
    for j in range(len(fuhao)):
        if s[i].find(fuhao[j]) != -1:
            if s[i].find(fuhao[j]) != len(s[i]) - 1:
                s[i] = "4"
            if len(s[i])>=3:
                if s[i].find("-")== len(s[i])-2:
                    s[i]="3"

for i in range(len(s)):
    if s[i] != "1" and s[i] != "2" and s[i] != "3" and s[i] != "4":
        num = num + 1
print(s)
print(num)
