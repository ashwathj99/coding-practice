class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        results = []
        if n==1:
            results.append(0)
        def recurse(current, last_digit, digits_left):
            if digits_left==0:
                results.append(current)
                return

            new_digit = last_digit + k
            if new_digit<=9 and k!=0:                                               #k!=0 to handle duplicates
                    recurse(current*10 + new_digit, new_digit, digits_left-1)
            new_digit = last_digit - k
            if new_digit>=0:
                recurse(current*10 + new_digit, new_digit, digits_left-1)

        for first_digit in range(1,10):
            recurse(first_digit,first_digit,n-1)

        return sorted(results)