def q26(nums):
    if not nums:
        return 0

    n = len(nums)
    fast = slow = 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow

print(q26([1,1,2]))
