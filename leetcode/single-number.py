class Solution:
    def singleNumber(self, nums) -> int:
        return 2*sum(set(nums)) - sum(nums)

    """
    Alternative solution //Bit manipulation quiccc
    int singleNumber(int A[], int n)
    {
        int result = 0;
        for (int i = 0; i<n; i++)
        {
            result ^=A[i];
        }
        return result;
    }
"""