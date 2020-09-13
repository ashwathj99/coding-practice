class Solution:
    import math
    def countBits(self, num: int):
        dp = [0]
        for i in range(1,num+1):
            dp.append(dp[i//2] + i%2)
        return dp
#         1       1         1
#         2       10        1
#         3       11        2
#         4       100       1
#         5       101       2
#         6       110       2
#         7       111       3
#         8       1000      1
#         9       1001      2
#         10      1010      2
#         11      1011      3
#         12      1100      2
#         12      1101      3
#         14      1110      3
#         15      1111      4