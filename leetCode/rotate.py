def rotate(list,k):
    for i in range(k):
        list.insert(0, list.pop(-1))
    return list

print(rotate([1,2,3,4,5,6],3))