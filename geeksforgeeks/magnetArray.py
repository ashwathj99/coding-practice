from decimal import *
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    res = []
    x = l[0]
    while x<l[-1]+1:
        f1,f2 = [0,0]
        for i in l:
            if i<x:
                f1+=1/(x-i)
            elif i>x:
                f2+=1/(i-x)
        # if x==1.5: print(f1,f2)
        if f1==f2:  res.append(x)
        getcontext().prec = 2
        x+=Decimal(1/10)
    print(res)