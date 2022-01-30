properties = [[2,2],[3,3]]
num = 0
for i in range(len(properties)):
    for j in range(len(properties)):
        if properties[i][0]<properties[j][0] and properties[i][1]<properties[j][1]:
            num=num+1
            break
print(len(properties))
print(num)
