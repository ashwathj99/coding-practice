def absolutePermutation(n, k):
    l = list(range(1,n+1))
    if k==0:
        return l
    if n%2==1:
        return [-1]
    for i in range(n-k):
        if l[i]==l[i+k]-k:
            l[i],l[i+k] = l[i+k], l[i]
        elif abs(i+1-l[i])!=k:
            return [-1]
    for i in range(n-k,n):
        if(abs(i+1-l[i])!=k):
            return [-1]
    return l