def q75(nums):
    for j in range(3):
        for i in range(nums.count(j)):
            nums.append(nums.pop(nums.index(j)))
    return nums
print(q75( [2,0,2,1,1,0]))