def q1725(rectangles):
    l=[]
    for i in range(len(rectangles)):
        l.append(min(rectangles[i][0],rectangles[i][1]))
    return l.count(max(l))

print(q1725([[5,8],[3,9],[5,12],[16,5]]))