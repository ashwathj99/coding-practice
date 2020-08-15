#python matrices are fucked up
t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    str1, str2 = input().split()
    DP = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                DP[i][j] = i+j
            else:
                if str1[i-1]==str2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = 1 + min(DP[i-1][j],DP[i-1][j-1],DP[i][j-1])
    print(DP[m][n])