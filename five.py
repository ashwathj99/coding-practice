n = int(input())
#    print("hello")
l = []
flag = 0
if n<0 :
    flag = 1
    n = -1*n
while(n!=0):
    mod = n%10
    n = n//10
    l.append(mod)
l.sort()
#print(l)

swappos = 1
while(l[0]==0):
    temp = l[swappos]
    l[swappos]=0
    l[0]=temp
    swappos+=1
res = int("".join(map(str,l)))
if flag==1 :
    print(-1*res)
else:
    print(res)