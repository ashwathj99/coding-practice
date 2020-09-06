n = int(input())
# def minDays(n):
#     # maxeat = 1
#     days = 0
#     # n-=1
#     while n > 0:
#         # remaining = n
#         if n%2==0:        maxeat = n//2
#         elif n%3==0:      maxeat = 2*n//3
#         else:             maxeat = 1
#         print(maxeat, "a")
#         if maxeat > n:    return days+1
#         else:
#             n = n - maxeat
#             days+=1
#     return days
# print(minDays(n))
class Solution:
    def minDays(self, n: int) -> int:
        # @lru_cache        #memoize the recursive calls
        def recurse(n):
            if n==1:
                return 1
            if n%6==0:
                return 1 + min(recurse(n//3), recurse(n//2))
            if n%3==0:
                return 1 + min(recurse(n//3), recurse(n-1))
            if n%2==0:
                return 1 + min(recurse(n//2), recurse(n-1))
            return 1 + recurse(n-1)
        return recurse(n)