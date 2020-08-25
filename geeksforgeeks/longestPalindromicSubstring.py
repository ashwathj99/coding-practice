t = int(input())
# def longestPalindrome(s):   
#     m = ''
#     if len(s) == 1:
#         return s
#     for i in range(len(s)):
#         for j in range(len(s)+1):
#             if len(m) >= j-i:
#                 continue
#             elif s[i:j] == s[i:j][::-1]:
#                 m = s[i:j]
#                 continue
#     return m
def longestPalindrome(s):
    n = len(s)
    dp = [[0 for x in range(n)] for y in range(n)]
    maxLength = 1
    for i in range(n): dp[i][i] = True
    start, i = [0,0]
    while i < n-1:
        if s[i]==s[i+1]:
           dp[i][i+1]=True
           start = i
           maxLength = 2
        i+=1
    k = 3
    while k <= n:
        i = 0
        while i < n-k+1:
            j = i+k-1
            if dp[i+1][j-1] and s[i]==s[j]:
                dp[i][j] = True
                if k > maxLength:
                    start = i
                    maxLength = k
            i+=1
        k+=1
    if maxLength==2:
        for i in range(n-2):
            if s[i] == s[i+1]:
                start = i
                break
    return s[start:start+maxLength]
for _ in range(t):
    s = input()
    print(longestPalindrome(s))