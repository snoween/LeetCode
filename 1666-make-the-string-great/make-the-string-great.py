class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            # eE
            if stack and char.isupper() and stack[-1] == char.lower():
                stack.pop()
                continue
            
            # Ee
            elif stack and char.islower() and stack[-1] == char.upper():
                stack.pop()
                continue
            
            stack.append(char)
        
        return ''.join(stack)
                