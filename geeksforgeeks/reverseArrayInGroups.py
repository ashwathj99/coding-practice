t = int(input())
for _ in range(t):
    n,d = map(int,input().split())
    l = list(map(int,input().split()))
    temp = []
    res = []
    if d>=n:
        for i in l[::-1]:
            print(i, end = " ")
        print()
        continue
    for i in range(n):
        if (i+1)%d==0:
            temp.append(l[i])
            res.extend(temp[::-1])
            temp = []
        else:
            temp.append(l[i])
    res.extend(temp)
    for i in res:
        print(i, end = " ")
    print()