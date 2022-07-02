def q55(nums):

    for i in range(len(nums)):
        if nums[i]==0:
            for j in range(i):
                if i-j>=nums[j]:

    return True
print(q55([3,2,2,0,4]))