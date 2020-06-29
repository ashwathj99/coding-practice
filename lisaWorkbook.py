arr = [4,2,6,1,10]
# arr = [1,4,5]
k = 3
pagenum = 0
special = 0
for numq in arr:
    if numq<=k:
        pagenum+=1
        if pagenum in list(range(1,numq+1)):
            special+=1
    else:
        p = 0
        pagenum+=1
        for i in range(1,numq+1):
            p+=1
            print(numq, " ", i, " ", pagenum, " ", p)
            if i == pagenum:
                # print(numq, " ", i, " ", pagenum, " ", p)
                special+=1
            if (p%k==0):
                p = 0
                if i!=numq:
                    pagenum+=1 
print(pagenum)