#code
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    # for i in range(n-1):
    #     flag = 1
    #     for j in range(i+1,n):
    #         if l[i]<l[j]:
    #             flag = 0
    #             break
    #     if flag==1:
    #         print(l[i],end = " ")
    m = -1
    temp = []
    for i in range(n-1,-1,-1):
        if m<l[i]:
            m = l[i]
        print(m)
        if m<=l[i]:
            temp.append(l[i])
    for i in temp[::-1]:
        print(i, end = " ")
    print()