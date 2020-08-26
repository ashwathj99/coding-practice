for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    minmoves = 1000000000
    minpos = -1
    for start in l:
        distance = k - start
        if distance < 0: continue
        if distance % start == 0 :
            moves = distance//start
            if moves < minmoves:
                minmoves = moves
                minpos = start
    print(minpos)