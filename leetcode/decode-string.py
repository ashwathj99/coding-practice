class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currNum = 0
        currString = ''
        for char in s:
            if char == ']':
                stack.append(currString)
                stack.append(currNum)
                currString = ''
                currNum = 0
            elif char == '[':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num*currString
            elif char.isdigit():
                currNum = currNum*10 + char - '0'
            else:
                currString+=char
        return currString