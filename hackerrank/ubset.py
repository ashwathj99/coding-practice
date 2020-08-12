s = [19,10,12,10,24,25,22]
l = []
k = 4
for i in range(len(s)):
    val = s[i]
    for j in range(len(s)):
        if(i!=j):
            if((s[i]+s[j])%k!=0):
                l.append([s[i],s[j]])
for i in s:
    for j in range(len(l)):
        count = 0
        for ele in l[j]:
            if(ele%k!=0):
                count+=1
        if(count==len(l[j]) and i not in l[j]):
            l[j].append(i)
        for q in range(len(l)):
            if q!=j:
                if((s[j]+s[q])%k!=0):
                    count+=1
            # if count==len()
        
l2 = []
for i in l:
    for j in i:
        l2.append(j)
# for i in l:
#     for 
