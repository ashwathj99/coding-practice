class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        n = len(arr)
        for start in range(n):
            # print('start = ', start, arr[start:start+m*k], arr[start:start+m]*k)
            if arr[start:start+m*k]==arr[start:start+m]*k:
                return True
        return False