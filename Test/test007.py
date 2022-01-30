s = input().split()
b1 = int(s[0])
b2 = int(s[1])
m1 = int(s[2])
m2 = int(s[3])
a1 = 0
a2 = 0
m = [[m1, m2]]
if m2 - 2 >= 0 and m1 - 1 >= 0:
    m.append([m2 - 2, m1 - 1])
if m2 + 2 <= 20 and m1 - 1 >= 0:
    m.append([m2 + 2, m1 - 1])
if m2 - 1 >= 0 and m1 - 2 >= 0:
    m.append([m2 - 1, m1 - 2])
if m2 + 1 <= 20 and m1 - 2 >= 0:
    m.append([m2 + 1, m1 - 2])
if m2 - 2 >= 0 and m1 + 1 <= 20:
    m.append([m2 - 2, m1 + 1])
if m2 - 1 >= 0 and m1 + 2 <= 20:
    m.append([m2 - 1, m1 + 2])
if m2 + 1 <= 20 and m1 + 2 <= 20:
    m.append([m2 + 1, m1 + 2])
if m2 + 2 <= 20 and m1 + 1 <= 20:
    m.append([m2 + 2, m1 + 1])

