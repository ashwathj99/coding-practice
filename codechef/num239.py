for _ in range(int(input())):
    l, r = map(int, input().split())
    count = 0
    for i in range(l, r+1):
        s = str(i)[-1]
        if s in ['2','3','9']:
            count+=1
    print(count)