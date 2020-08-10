s = "asasd"
s = "mnonopoo"
s = "abcbaba"
# s = "aaaa"
n = len(s)
l = []
count = 0
curr = None
for i in range(n):
    if s[i]==curr:
        count+=1
    else:
        if curr is not None:
            l.append((curr,count))
        curr = s[i]
        count = 1
l.append((curr,count))
print(l)

count = 0
for i in l:
    count+=i[1]*(i[1]+1)//2

for i in range(1,len(l)-1):
    if(l[i-1][0]==l[i+1][0] and l[i][1]==1):
        count+=min(l[i-1][1],l[i+1][1])
print(count)
