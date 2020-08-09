#code
t = int(input())
for _ in range(t):
    n,d = map(int,input().split())
    l = list(map(int,input().split()))
    l.extend(l)
    for i in range(n):
        print(l[i+d],end = " ")
    print()
    # print(l[:n])