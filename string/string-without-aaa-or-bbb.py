class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        stack = []

        while a > 0 or b > 0:
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                if stack[-1] == 'a':
                    stack.append('b')
                    b -= 1
                else:
                    stack.append('a')
                    a -= 1
            else:
                if a > b:
                    stack.append('a')
                    a -= 1
                else:
                    stack.append('b')
                    b -= 1
        
        return ''.join(stack)