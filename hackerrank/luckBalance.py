balance = 0
l = []
# contests = [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]
contests = [[5,1],[4,0],[6,1],[2,1],[8,0]]

# k = 3
k = 2
for i in contests:
    if (i[1]==0):
        balance+=i[0]
        # if k>0: k-=1
            
    else:
        l.append(i[0])
l.sort(reverse=True)
# print(l)
# print(k)
# sub = sum(l[:k-1])
# s = sum(l[k-1:])
sub = 0
for i in range(len(l)):
    if i<k:
        balance+=l[i]
        # print("add this",l[i])
    else:
        balance-=l[i]
        # print("sub", l[i])

# print("balance ", balance)
# print("s ", s)
# print("sub ", sub)
# print(balance + s - sub)
# arr = [13,10,9,8,13,12,18,13]
# print(sorted(arr))
