def q1405(a, b, c):
    s = " "
    while a > 0 or b > 0 or c > 0:
        if a >= b and a >= c:
            if s[len(s) - 1] != "a":
                if a >= 2:
                    s = s + "aa"
                    a = a - 2
                    continue
                if 0 < a < 2:
                    s = s + "a"
                    a = a - 1
                    continue
            if s[len(s) - 1] != "b" and b>0:
                s = s + "b"
                b = b - 1
                continue
            if s[len(s) - 1] != "c" and c>0:
                s = s + "c"
                c = c - 1
                continue
        if b >= a and b >= c:
            if s[len(s) - 1] != "b":
                if b >= 2:
                    s = s + "bb"
                    b = b - 2
                    continue
                if 0 < b < 2:
                    s = s + "b"
                    b = b - 1
                    continue
            if s[len(s) - 1] != "a" and a>0:
                s = s + "a"
                a = a - 1
                continue
            if s[len(s) - 1] != "c" and c>0:
                s = s + "c"
                c = c - 1
                continue
        if c >= a and c >= b:
            if s[len(s) - 1] != "c":
                if c >= 2:
                    s = s + "cc"
                    c = c - 2
                    continue
                if 0 < c < 2:
                    s = s + "c"
                    c = c - 1
                    continue
            if s[len(s) - 1] != "a" and a>0:
                s = s + "a"
                a = a - 1
                continue
            if s[len(s) - 1] != "b" and b>0:
                s = s + "b"
                b = b - 1
                continue
        return s[1:len(s)]
    return s[1:len(s)]

print(q1405(7, 1, 0))
