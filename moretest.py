
import numpy 
  

def maxMin(iterable, r): 
    print("inside")
      
    char = tuple(iterable) 
    n = len(char) 
      
    if r > n: 
        return
      
    index = numpy.arange(r) 
      
    # retruns the first sequence
    m = 10000
    f = tuple(char[i] for i in index) 
    diff = max(f)-min(f)
    if diff<m:
        m = diff
    print("here")
    l = []
    flag = 1
    while flag: 
          
        for i in reversed(range(r)): 
            if index[i] != i + n - r: 
                break
            else:
                flag = 0
                break
                l.append(diff)
        if not flag:
            break
          
        index[i] += 1
          
        for j in range(i + 1, r): 
              
            index[j] = index[j-1] + 1
              
        t = tuple(char[i] for i in index)
        diff = max(t)-min(t)
        print(diff)
        if diff<m:
            m = diff
    print("e")
    print(diff)
    print(l)
    # print("end")
    return "HELLO"
          
# Driver code 
arr = [10,100,300,200,1000,20,30]
k = 3
print(maxMin(arr,k))
