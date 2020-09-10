class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Two Pointer Approach
        l = 0
        r = len(s)-1
        while l < r:
            s[l],s[r] = s[r], s[l]
            l+=1
            r-=1