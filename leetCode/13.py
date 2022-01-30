s = "MCMXCIV"
num=0
temp=s[0]
i0=0
temparr=[]
temparr2=[]
ch = "IVXLCDM"
for i in range(len(s)):
    if s[i]!=temp:
        temparr.append(s[i0:i])
        temp=s[i]
        i0=i
    if i ==len(s)-1:
        temparr.append(s[i0:len(s)])
print(temparr)
for i in range(len(temparr)):
    for j in range(len(ch)):
        if temparr[i][0] ==ch[j]:
            temp=""
            for k in range(len(temparr[i])):
                temp = str(j)+temp
            temparr2.append(temp)
print(temparr2)

for i in range(len(temparr2)):
    if i<len(temparr2)-1:
        if temparr2[i]>temparr2[i+1] :
            for  j in range(len(temparr2[i])):
                if temparr2[i][0]=='0':
                    num=num+1
                if temparr2[i][0]=='1':
                    num=num+5
                if temparr2[i][0]=='2':
                    num=num+10
                if temparr2[i][0] == '3':
                    num = num + 50
                if temparr2[i][0] == '4':
                    num = num + 100
                if temparr2[i][0] == '5':
                    num = num + 500
                if temparr2[i][0] == '6':
                    num = num + 1000
        if temparr2[i]<temparr2[i+1] :
            for  j in range(len(temparr2[i])):
                if temparr2[i][0]=='0':
                    num=num-1
                if temparr2[i][0]=='1':
                    num=num-5
                if temparr2[i][0]=='2':
                    num=num-10
                if temparr2[i][0] == '3':
                    num = num - 50
                if temparr2[i][0] == '4':
                    num = num - 100
                if temparr2[i][0] == '5':
                    num = num - 500
                if temparr2[i][0] == '6':
                    num = num - 1000
    if i ==len(temparr2)-1:
        for j in range(len(temparr2[i])):
            if temparr2[i][0] == '0':
                num = num + 1
            if temparr2[i][0] == '1':
                num = num + 5
            if temparr2[i][0] == '2':
                num = num + 10
            if temparr2[i][0] == '3':
                num = num + 50
            if temparr2[i][0] == '4':
                num = num + 100
            if temparr2[i][0] == '5':
                num = num + 500
            if temparr2[i][0] == '6':
                num = num + 1000
print(num)