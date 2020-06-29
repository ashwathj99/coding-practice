def fairRations(B):
    count = 0
    for i in range(len(B)):
        if B[i]%2==1:
            if i==len(B)-1:
                return "NO"
            else:
                B[i], B[i+1] = B[i]+1, B[i+1]+1
                count+=1
    return count*2