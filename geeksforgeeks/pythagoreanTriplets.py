#code
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    flag = 0
    d = {x**2:x for x in sorted(l)}
    for i in d:
        for j in d:
            if i!=j and i+j in d:
                flag = 1
                break
    if flag ==1: print("Yes")
    else: print("No")