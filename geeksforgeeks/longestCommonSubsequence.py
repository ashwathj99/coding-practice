t = int(input())
def LCS(X , Y, m, n):
    L = [[0]*(n+1) for i in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n] 
for _ in range(t):
    m,n = map(int,input().split())
    str1 = input()
    str2 = input()
    print(LCS(str1,str2,m,n))