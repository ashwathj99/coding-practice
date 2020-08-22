# brute force
# def checker(i):
#     s = str(i)
#     n = len(s)
#     for i in range(1,n):
#         if abs(int(s[i]) - int(s[i-1]))!=1:
#             return False
#     return True
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     for i in range(min(11,n)):
#         print(i, end = " ")
#     for i in range(12,n):
#         if(checker(i)):
#             print(i)
# optimized
#Class queue for use later 
class Queue: 
    def __init__(self): 
        self.lst = [] 
  
    def is_empty(self): 
        return self.lst == [] 
  
    def enqueue(self, elem): 
        self.lst.append(elem) 
  
    def dequeue(self): 
        return self.lst.pop(0)

def bfs(x, num, res):
    q = Queue() 
    q.enqueue(num)
    while (not q.is_empty()): 
        num = q.dequeue() 
  
        if num<= x:
            res.append(num)
            last_dig = num % 10
            if last_dig == 0: 
                q.enqueue((num * 10) + (last_dig + 1))
            elif last_dig == 9: 
                q.enqueue((num * 10) + (last_dig - 1)) 
 
            else: 
                q.enqueue((num * 10) + (last_dig - 1)) 
                q.enqueue((num * 10) + (last_dig + 1))

def printJumping(x):
    res = [0]
    for i in range(1, 10): 
        bfs(x, i, res) 
    for num in sorted(set(res)):
        print(num, end = " ")
t = int(input())
for _ in range(t):
    n = int(input())
    printJumping(n) 
    print()