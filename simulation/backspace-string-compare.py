class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checkBackspace(s: str):
            stack = []
            for char in s:
                if stack and char == "#":
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return ''.join(stack)
        
        return checkBackspace(s) == checkBackspace(t)