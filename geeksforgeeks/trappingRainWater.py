#brute-force
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     total = 0
#     for i in range(1,n):
#         left = max(l[:i])
#         right = max(l[i:])
#         m = min(left,right)
#         if m>l[i]:  total+=m-l[i]
#     print(total)
#optimized
n = 6
# l = [8,8,2,4,5,5,2]
l = [3,0,0,2,0,4]
left = [l[0]]
m1 = l[0]
total = 0
for i in range(1,n):
    if l[i]>m1:     m1 = l[i]
    left.append(m1)
right = []
m2 = -1
for i in range(n-1):
    if l[::-1][i]>m2:   m2 = l[::-1][i]
    right.append(m2)
right.append(l[0])
right = right[::-1]
for i in range(n):
    total+=(min(left[i],right[i])-l[i])
print(total)