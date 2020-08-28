t = int(input())
def numDigits(num):
    if num % 9 :
        return  num//9 + 1
    return pc//9 
for _ in range(t):
    pc, pr = map(int, input().split())
    minChef = numDigits(pc)
    minRick = numDigits(pr)
    if minChef<minRick:
        print(0,minChef)
    else:
        print(1,minRick)