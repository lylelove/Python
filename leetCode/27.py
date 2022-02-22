def q27(nums,val):
    a=len(nums)
    if not nums:
        return 0
    for i in range(len(nums)):
        if nums[i]==val:
            nums[i]=51
            a=a-1
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                temp = nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums,a

print(q27( [0,1,2,2,3,0,4,2],2))