def zero(nums):
    for i in range(nums.count(0)):
        nums.pop(nums.index(0))
        nums.append(0)
    return nums
print(zero([0,1,0,2,3,0,4,5]))