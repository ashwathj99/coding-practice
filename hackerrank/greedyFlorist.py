k = 3
# k = 2
c = [2,5,6]
# c.sort(reverse=True)
# d = {i+1 : 0 for i in range(k)}
# products = {i+1 : [] for i in range(k)}
# f = [0]*len(c)
# count = 0
# # prices = []
# if len(c)<k:
#     print(sum(c))
# else:
#     tobuy = len(c)
#     i = 0
#     while tobuy>k:
#         price+=
#         i+=1
# while count<3:
#     # prices = []
#     # m = [1000,1000,1000,1000]
#     # price = 1000
#     for key in d:
#         while()
#         products[key].append(c[-1])

#         d[key]+=1

        
        # for i in range(len(c)):
        #     if f[i]==0:

        #         price = c[i]*(d[key]+1)
        #         if price<m[3]:
        #             m = [key,i,c[i],price]
    # d[m[0]]+=1
    # f[m[1]]=1
    # count+=1
    # print(m)
c.sort(reverse=True)
cost = 0
previous_purchase = 0
for i in range(k):
    cost += (previous_purchase +1) * c[i]
    if (i+1)%k==0:
        previous_purchase += 1
print(cost)
