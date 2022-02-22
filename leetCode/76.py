# def q76(s,t):
#     minl = len(s)
#     res = ""
#     ci = True
#     for i in range(len(t)):
#         if s.count(t[i]) == 0:
#             ci = False
#     while ci:
#         fir=[]
#         for i in range(len(t)):
#             fir.append(s.index(t[i]))
#         fir=sorted(fir)
#         if fir[len(fir)-1]-fir[0]<=minl:
#             res = s[fir[0]:fir[len(fir)-1]]
#         s=s[fir[0]:]
#         for i in range(len(t)):
#             if s.count(t[i])==0:
#                 ci=False
#
#     return res




print(q76("aa","aa"))