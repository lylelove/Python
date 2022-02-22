def q1748(nums):
    i=0
    for j in range(len(nums)):
        if nums.count(nums[j])==1:
            i = i+nums[j]
    return i
print(q1748([1,2,2,3]))