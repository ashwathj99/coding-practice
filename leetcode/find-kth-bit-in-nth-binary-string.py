def findKthBit(n, k):
    i = 0
    s = ""
    while(i < n):
        i+=1
        if i==1:
            s+='0'
            continue
        temp = ''.join('1' if ch =='0' else '0' for ch in s)
        s+='1'+temp[::-1]
        print(s)
    return s
        
        

n, k = 2, 3
print(findKthBit(n,k)[k-1])