class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        d = {i:0 for i in range(1, n+2)}
        for i in nums:
            if i in d:
                d[i] = 1
        lst = []
        for i in d:
            if d[i]==0 and i>0:
                lst.append(i)
        print(d)
        print(lst)
        return min(lst)