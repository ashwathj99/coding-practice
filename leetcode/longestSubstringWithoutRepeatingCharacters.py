s = "abcbda"
n = len(s)
i = 0
maxLength = 0
start = i
d = {}
while i < n:
    if s[i] in d:
        i = start + 1
        d = {}
        start = i
    else:
        d[s[i]] = 1
        i+=1
        if len(d) > maxLength:
            maxLength = len(d)
    # print(d)
print(maxLength)
