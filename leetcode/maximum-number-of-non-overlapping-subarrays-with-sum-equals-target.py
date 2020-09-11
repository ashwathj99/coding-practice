
# target = 79
nums = [1,1,1,1,1]
target = 2
# nums = [0,0,0]
# target = 0
def subarrays(nums, target):
    n = len(nums)
    subs = []
    for i in range(n):
        curr = [0 for x in range(n)]
        for j in range(i,n):
            curr[j] = curr[j-1] + nums[j]
            if curr[j]==target:
                subs.append([i,j])
    return subs
def nonOverlap(l):
    l.sort(key = lambda x : (x[1], x[0]))
    res = []
    latest = -1000
    for i in range(len(l)):
        start, end = l[i]
        if start < latest+1:
            continue
        else:
            latest = max(latest, end)
            res.append([start,end])
    print(l)
    return res
    # print(dp)
subs = subarrays(nums, target)
print(subs)
print("Phew")
res = nonOverlap(subs)
print(res)