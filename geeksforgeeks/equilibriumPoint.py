t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    f = 0
    s1 = l[0]
    s2 = sum(l[1:])
    if len(l)==1:
        print(1)
        f=1
    for i in range(1,n):
        s1+=l[i]
        if s1==s2:
            print(i+1)
            f = 1
        s2-=l[i]
    if f==0: print(-1)
    