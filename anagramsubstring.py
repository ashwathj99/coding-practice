from collections import *
s = "abbababba"
check = defaultdict(int)
l = len(s)
for i in range(l):
    for j in range(i+1,l+1):
        sub = list(s[i:j])
        sub.sort()
        sub = "".join(sub)
        check[sub]+=1
summ = 0
for i in check:
    print(i)
    n = check[i]
    summ += (n*(n-1))//2
print(summ)
print(check)