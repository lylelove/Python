def q88(nums1,nums2):
    for i in range(len(nums2)):
        nums1[nums1.index(0)]=nums2[i]
        nums1.sort()
    return nums1
print(q88([1,2,3,0,0,0],[1,2,7]))