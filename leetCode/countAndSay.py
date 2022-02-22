def countAndSay(n: int):
    if n == 1:
        return '1'
    s = countAndSay(n - 1)

    ans = ''
    start, end = 0, 0
    while end < len(s):
        while end < len(s) and s[start] == s[end]:
            end += 1
        ans += str(end - start) + s[start]
        start = end

    return ans

s=[]
for i in range(1,31):
    s.append(countAndSay(i))
print(s)