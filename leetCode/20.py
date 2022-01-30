def q20(s):
    ch = ["(}","(]","{)","{]","[)","[}"]
    # if len(s)%2==1:
    #     return False
    # for i in range(len(ch)):
    #     if ch[i] in s:
    #         return False
    # ch = "(){}[]"
    # s0 = []
    # for i in range(len(s)):
    #     if s[i] == "(":
    #         s0.append(1)
    #     if s[i] == ")":
    #         s0.append(-1)
    #     if s[i] == "{":
    #         s0.append(2)
    #     if s[i] == "}":
    #         s0.append(-2)
    #     if s[i] == "[":
    #         s0.append(3)
    #     if s[i] == "]":
    #         s0.append(-3)
    # temp =0
    # for i in range(len(s0)):
    #     temp=temp+s0[i]
    # if temp!=0:
    #     return False
    # ch = [")(","}{","]["]
    # for i in range(len(ch)):
    #     if ch[i] in s:
    #
    # return True


print(q20("()}{()"))
