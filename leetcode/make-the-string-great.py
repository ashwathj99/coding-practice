class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for letter in s:
            if not result:
                result.append()
            elif result[-1].isupper() and result[-1].lower() == letter:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == letter:
                result.pop()
            else:
                result.append(letter)
        return ''.join(result)