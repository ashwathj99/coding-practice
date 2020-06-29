t = int(input())
l = []
for i in range(t):
    n = int(input())
    for j in range(2*n):
        l.append(list(map(int,input().split())))
    print(l)
    new = []
    k = 0
    for element in l:
        for ele in element:
            new.append(ele)
    print(new)
    j = 0
    new2 = []
    while(j<=len(new)):
        try:
            new2.append(new[j]-new[j+1])
            j+=2
        except:
            break
    print(new2)
    new2.sort(reverse = True)
    print(sum(new2[0:n]))