import numpy as np
t = int(input())
matrix = [[1,0,1],[1,0,1],[1,1,1],[0,0,1]]
print(matrix)
# for i in range(t):
#     m,n = map(int,input().split())
#     values = list(map(int,input().split()))
#     matrix = np.array(values).reshape(m,n)
#     print(matrix)
colors = 0
count = 0
for i in range(m):
    for j in range(n):
        val = matrix[i][j]
        if(val==0):
            continue
        else:
            count+=1
            if(count>1):
                l1 = matrix[0:i]
                l2 = [ele[j] for ele in matrix[0:i][0:j]]
                if(val in l1 and val in l2):
                    matrix[i][j]=colors+=1
                    



