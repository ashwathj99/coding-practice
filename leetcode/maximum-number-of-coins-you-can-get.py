def func(piles):
    n = len(piles)
    piles.sort()
    count = 0
    curr = n//3
    while curr < n:
        count+=piles[curr]
        curr+=2
    print(count)
l = [2,4,1,2,7,8]
l = [9,8,7,6,5,1,2,3,4]
func(l)