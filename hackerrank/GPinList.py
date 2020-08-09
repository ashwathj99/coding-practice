arr = [1,3,9,9,27,81]
arr = [1,5,5,25,125]
arr = [1,2,2,4]
left = {val:arr.count(val) for val in set(arr)}
right = {val:arr.count(val) for val in set(arr)}
count = 0
r = 2
for num in arr:
    right[num]-=1
    try:
        c1 = right[num*r]
        c2 = left[num/r]
        count+=c1*c2
    except:
        gg=0
        #print(num)    
    left[num]+=1
print(count)
