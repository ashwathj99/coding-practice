arr = [10,100,300,200,1000,20,30]
k = 3
# arr= [1,2,3,4,10,20,30,40,100,200]
# k = 4
# arr = [1,2,1,2,1]
# k = 2
m = 1000
arr.sort()
for i in range(len(arr)-k+1):
    a = arr[i]
    b = arr[i+k-1]
    if m > b-a:
        m = b-a


print(m)
