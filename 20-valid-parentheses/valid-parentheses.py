class Solution:
    def isValid(self, s: str) -> bool:
        bracket = { ')': '(',
                    ']': '[',
                    '}': '{'}
        stack = []

        for element in s:
            if element not in bracket:
                stack.append(element)
            else:
                if stack and bracket[element] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack