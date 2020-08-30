def func(n):
    s = str(n)[::-1]
    res = ''
    f = 0
    if len(s)>3: f= 1

    for i in range(len(s)):
        res+=s[i]

        if i+1<len(s) and f and (i+1)%3 == 0:
            res+='.'
    return res[::-1]

print(func(123456789))