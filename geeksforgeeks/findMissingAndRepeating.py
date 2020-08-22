import math
t = int(input())
for _ in range(t):
    n = int(input())
    sum3 = n*(n+1)//2
    sum4 = n*(n+1)*(2*n + 1)//6
    sum1 = 0
    sum2 = 0
    for val in input().split():
        sum1+=int(val)
        sum2+=int(val)**2
    diff = sum1 - sum3
    add = (sum2-sum4)//diff
    b = (add + diff)//2
    a = (add - diff)//2
    print(b, a)