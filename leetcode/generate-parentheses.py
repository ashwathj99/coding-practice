class Solution:
    def generateParenthesis(self, n: int):
        # 1 1 ()
        # 2 2 ()() (())
        # 3 4 ()()() (())() ()(()) ((())) (()())
        # 4 6 ()()()()
        dp = [[] for i in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                dp[i]+=['(' + x + ')' + y for x in dp[j] for y in dp[i-j-1]]
        # print(dp[n])
        return dp[n]