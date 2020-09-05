class Solution:
    def findAnagrams(self, s: str, p: str):
        d = {i:p.count(i) for i in p}
        temp = {i:s[:len(p)].count(i) for i in s[:len(p)]}
        if len(p)>len(s): return []
        first = s[0]
        res = []
        for i in range(len(s) - len(p) + 1):
            if d==temp:
                res.append(i)
            try:
                temp[first]-=1
                if temp[first]==0:
                    temp.pop(first) 
                first = s[i+1]
                last = s[i+len(p)]
                if last in temp:
                    temp[last]+=1
                else:
                    temp[last] = 1 
            except:
                first = s[i]
        return res