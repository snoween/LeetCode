class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checkStr(s):
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack and char == '#':
                    stack.pop()
            return ''.join(stack)
        
        return checkStr(s) == checkStr(t)
