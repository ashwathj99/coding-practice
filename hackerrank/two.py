import numpy as np
n = int(input())
l = []
for i in range(n):
    row = list(map(int,input().split()))
    l.append(row)
#print(l)
count = 0
def mysort(val): 
    return val[0]  
l.sort(key = mysort,reverse = True)
print(l)
for i in range(n):
    for j in range(n):
        if(i!=j):
            try:
                l1 = l[i]
                l2 = l[j]
                c = 0
                for ele in range(4):
                    if(l1[ele]>=l2[ele]):
                        break
                    else:  
                        c+=1
                if (c==4):
                    count+=1
                    l = np.delete(l,i,axis=0)
                    l.sort(key = mysort,reverse = True)
                    # print(i,j)
                    # print()
            except:
                g=0
print(count)
