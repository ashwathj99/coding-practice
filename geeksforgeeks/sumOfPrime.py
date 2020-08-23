def Sieve(n, isPrime): 
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1): 
        isPrime[i] = True
    num = 2
    while(num*num <= n):
        if (isPrime[num] == True):
            i = num*num 
            while(i <= n): 
                isPrime[i] = False
                i += num 
        num += 1
def func(n):
    isPrime = [0] * (n+1) 
    Sieve(n, isPrime)
    for i in range(0, n):
        if (isPrime[i] and isPrime[n - i]):
            print(i,(n - i)) 
            return
    print(-1)
    return
for _ in range(int(input())):
    n = int(input())
    func(n)