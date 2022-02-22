def q84(heights):
    hei=[]
    for i in range(max(heights)):
        tiao =[]
        while heights.count(i)>1:
            temp=[]
            for j in range(heights.index(i)):
                temp.append(heights[j])
            tiao.append(temp)

print(q84([2,4]))