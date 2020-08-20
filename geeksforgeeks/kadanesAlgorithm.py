t = int(input())
# t = 1
# l = [-2, -3, 4, -1, -2, 1, 5, -3]
# -2 -2 4 [4,-1] [4,-1,-2] [4,-1,-2,1] 
# n = len(l)
def MaxSubSum(l,n):
    max_so_far = -100000000000000
    max_ending_here = 0
    for i in range(n):
        max_ending_here = max_ending_here + l[i]
        print(max_so_far,max_ending_here, end = "\t")
        if(max_so_far<max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here<0:
            max_ending_here=0
        print(max_so_far,max_ending_here)
    return max_so_far
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(MaxSubSum(l,n))