def findLatestStep(arr, m):
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res
arr = [3,1,5,4,2]
m = 1
print(findLatestStep(arr, m))