intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,6],[2,3],[4,5]]
def func(intervals):
    intervals.sort(key = lambda x :(x[1], x[0]))
    count = 0
    latest = -10000
    for start, end in intervals:
        if start < latest:
            count+=1
        else:
            latest = max(latest, end)
    return count
print(func(intervals))