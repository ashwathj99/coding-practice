import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):
    grid =  [[1 if x=='G' else -1 for x in row] for row in grid]
    r = len(grid)
    c = len(grid[0])
    l = []
    res = []
    res.append(find(grid,l,r,c))
sub = []
def find(grid,l,r,c):
    for i in range(1,r-1):
        for j in range(1,c-1):
            if grid[i][j]==1:
                left,right,up,down = j,j,i,i
                grid[i][j]=0
                length = 0
                while left-1>=0 and right+1<=c-1 and up-1>=0 and down+1<=r-1:
                    left,right,up,down = left-1,right+1,up-1,down+1
                    if [grid[i][left],grid[i][right],grid[up][j],grid[down][j]]==[1]*4:
                        grid[i][left]=0
                        grid[i][right]=0
                        grid[up][j]=0
                        grid[down][j]=0
                        length+=1
                    else:
                        sub.append(length)
                        find(grid,l,r,c)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    # result = twoPluses(grid)
    twoPluses(grid)
    # print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
