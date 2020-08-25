def findElement(l, n):
    m1, m2 = [l[0], l[-1]]
    left,right = [[],[]]    
    for i in range(1,n-1):
        if l[i]>m1:     m1 = l[i]
        left.append(m1)             #left has max element till that iteration index[1 to n-2]
    for j in range(n-2,0,-1):
        if l[j]<m2:     m2 = l[j]
        right.append(m2)            #right has min element till that iteration index[n-2 to 1]
    right = right[::-1]
    for i in range(len(left)):
        if left[i]<=l[i+1] and right[i]>=l[i+1]:
            return l[i+1]
    return -1
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    res = findElement(l,n)
    print(res)