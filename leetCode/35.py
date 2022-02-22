def q35(nums,target):
    if nums.count(target)>=1:
        return nums.index(target)
    else:
        nums.append(target)
        nums=sorted(nums)
        return nums.index(target)
print(q35([1,3,5,6],2))