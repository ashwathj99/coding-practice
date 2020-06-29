def minimumSwaps(arr):
    # if(sorted(arr)==arr): return 0
    # arr= [e-1 for e in arr]
    # swap = 0
    # count=0
    # for i, val in enumerate(arr):
    #     if(i!=val):
    #         pos = arr.index(i) #2
    #         count+=pos
    #         arr[i],arr[pos] = arr[pos], arr[i]
    #         swap+=1
    #     print(count)
    # return swap
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        # pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps