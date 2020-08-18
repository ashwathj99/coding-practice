import numpy as np
# def isValidSudoku(matrix):

R,C = [9,9]
t = int(input())
for _ in range(t):
    entries = list(map(int, input().split())) 
    matrix = np.array(entries).reshape(R, C) 
    # print(isValidSudoku(matrix))