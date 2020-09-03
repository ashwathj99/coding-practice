class Solution:
    def toGoatLatin(self, S: str) -> str:
        l = S.split(' ')
        res = ''
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(l)):
            word = ''
            first_letter = l[i][0]
            if first_letter in vowels:
                word+=l[i]
            if 65 <=ord(first_letter.upper())<=90 and first_letter not in vowels:
                word+=l[i][1:]+first_letter
            word+='ma'+'a'*(i+1)
            res+=word+' '
        return res[:-1]