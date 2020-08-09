#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):
    grid =  [[1 if x=='G' else 0 for x in row] for row in grid]
    r = len(grid)
    c = len(grid[0])
    count = 0
    for i in range(r):
        count+=grid[i].count(1)
    if count<2: return 0
    # if r<4 and c<4 and r+c!=6: return 1
    small = 0
    big = 0
    l = []
    startgrid = grid
    for i in range(1,r):
        for j in range(1,c):
            if grid[i][j]==1:
                left,right,up,down = j,j,i,i
                grid[i][j]=-1
                length = 0
                while left-1>=0 and right+1<=c-1 and up-1>=0 and down+1<=r-1:
                    left,right,up,down = left-1,right+1,up-1,down+1
                    if [grid[i][left],grid[i][right],grid[up][j],grid[down][j]]==[1]*4:
                        grid[i][left]=-1
                        grid[i][right]=-1
                        grid[up][j]=-1
                        grid[down][j]=-1
                        length+=1
                    else:
                        grid = startgrid
                        break
                # if length==1:
                #     print(i,j, length)
                l.append([i,j,length])
                # if [small,big]==[0,0]:
                #     big = length
                # if length>1:
                #     if length==big and length>small:
                #         small = length
                #     if length>small and length<big:
                #         small = length
                #     elif length>big:
                #         big = length
    # if small==0 and big==0: return 1
    l.sort(key = lambda x:x[-1])
    # newl = [x for x in l if x[-1]>0]
    print(l)
    small,big = l[-2][-1],l[-1][-1]
    a1 = small*4+1
    a2 = big*4+1
    # return a1*a2
    print("res =",a1*a2)



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
