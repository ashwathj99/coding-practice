t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if sorted(l)[::-1] == l:
        print("No Profit")
        continue
    curr = 0
    res = []
    for i in range(n-1):
        if l[i+1] >= l[i] and curr == 0:
            buy, curr = [i, 1]
        if l[i+1] < l[i] and curr == 1:
            res.append([buy, i])
            curr, buy=[0,i+1]
    if curr == 1 and l[i+1] >= l[i]:
        res.append([buy,i+1])
    for i,j in res:
        print("("+str(i)+" "+str(j)+")", end = " ")
    print()