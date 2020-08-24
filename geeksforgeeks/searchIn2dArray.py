def search(l,num,i,j):
    if i==j:
        return searchval(l,num,i,0,len(l[0])-1)
    if num>l[i][-1]:
        return search(l,num,i+1,j)
    if num<l[j][0]:
        return search(l,num,i,j-1)
def searchval(l,num,row,i,j):
    if i==j:
        if l[row][i]==num:  return [row,j]
        return -1
    if num>l[row][i]:
        return searchval(l,num,row,i+1,j)
    if num<l[row][j]:
        return searchval(l,num,row,i,j-1)
l =  [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(search(l,20,0,len(l)-1))