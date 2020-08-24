t = int(input())
def parenthesisChecker(exp):
    stack = []
    for char in exp:
        if char in ['{','(','[']:
            stack.append(char)
        else:
            if len(stack)==0:
                return 0
            curr = stack.pop()
            if curr == '(':
                if char!=')':
                    return 0
            if curr == '[':
                if char!=']':
                    return 0
            if curr == '{':
                if char!='}':
                    return 0
    if len(stack)>0:
        return 0
    return 1
for _ in range(t):
    exp = list(input())
    if(parenthesisChecker(exp)):
        print("balanced")
    else:
        print("not balanced")