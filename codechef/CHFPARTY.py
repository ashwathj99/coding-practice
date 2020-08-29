for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    num = 0
    for i in l:
        if num>=i:
            num+=1
    print(num)