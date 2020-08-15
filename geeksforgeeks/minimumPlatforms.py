def minimumPlatforms(arr, dep, n):
    arr.sort()
    dep.sort()
    plat_temp = 1
    plat = 1
    i, j = [1,0]
    while i<n and j<n:
        if arr[i] <=dep[j]:
            plat_temp+=1
            i+=1
        elif arr[i]>dep[j]:
            plat_temp-=1
            j+=1
        if plat_temp > plat:
            plat = plat_temp
    print(plat)
t = int(input())
for _ in range(t):
    n = int(input())
    arrivals = input().split()
    departures = input().split()
    arrivals = [int(x) for x in arrivals]
    departures = [int(x) for x in departures]
    minimumPlatforms(arrivals, departures, n)