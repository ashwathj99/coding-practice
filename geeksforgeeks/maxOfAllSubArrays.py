# t = int(input())
# A for effort
# for _ in range(t):
#     n, k= map(int, input().split())
#     l = list(map(int, input().split()))
#     currmax = 0
#     for i in range(k):
#         if l[i]>currmax:
#             currmax = l[i]
#             maxpos = i
#     print(currmax, end = " ")
#     for i in range(k, n):
#         if i+1 > maxpos+k:
#             currmax = max(l[i-k+1:i+1])
#             print(currmax, end = " ")
#             continue
#         if l[i]>currmax:
#             currmax = l[i]
#             maxpos = i
#             print(currmax, end = " ")
#             continue
#         print(currmax, end = " ")
#     print()
from collections import deque 
t = int(input())
def printMax(arr, n, k):
    Qi = deque() 
    for i in range(k):
        arr[i] = int(arr[i])
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop()
        Qi.append(i)
    for i in range(k, n):
        arr[i] = int(arr[i])
        print(str(arr[Qi[0]]) + " ", end = "")
        while Qi and Qi[0] <= i-k:
            Qi.popleft() 
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop()
        Qi.append(i)
    print(str(arr[Qi[0]]))
for _ in range(t):
    n, k= map(int, input().split())
    printMax(input().split(),n,k)