t = int(input())
def printodd(n):
    number = 1
    for _ in range(n):
        for _ in range(n):
            print(number, end = " ")
            number = number + 1
        print()
def printeven(n):
    number = 1
    for i in range(n):
        l = []
        for _ in range(n):
            l.append(number)
            number = number + 1
        if i%2: l = l[::-1]
        for ele in l:
            print(ele, end = " ")
        print()

for _ in range(t):
    n = int(input())
    if n%2:     printodd(n)
    else:       printeven(n)