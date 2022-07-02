def guess(n):
    if n>1702766719:
        return -1
    if n<1702766719:
        return 1
    if n==1702766719:
        return 0
def q374(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if guess(mid) <= 0:
            right = mid  # 答案在区间 [left, mid] 中
        else:
            left = mid + 1  # 答案在区间 [mid+1, right] 中

    # 此时有 left == right，区间缩为一个点，即为答案
    return left
print(q374(2126753390))