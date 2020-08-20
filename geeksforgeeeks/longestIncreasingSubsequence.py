t = int(input())
def LIS(l,n):
    dp = [1]*n
    for i in range(1,n):
        j = 0
        temp = []
        while i!=j:
            if l[j]<l[i]:
                temp.append(dp[j]+1)
            j+=1
        # print(temp)
        if len(temp)>0:dp[i]=max(temp)
    # print(dp)
    return max(dp)
#dp stores lcs ending at that pos.
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(LIS(l,n))
    # LIS(l,n)
