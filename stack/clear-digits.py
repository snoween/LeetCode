class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for element in s:
            if element.isalpha():
                stack.append(element)
            else:
                stack.pop()
        
        return ''.join(stack)