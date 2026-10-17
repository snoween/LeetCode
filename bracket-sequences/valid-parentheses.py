class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for element in s:
            if element not in brackets:
                stack.append(element)
            else:
                if stack and brackets[element] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack