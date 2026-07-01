class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            if stack and digit < stack[-1] and k > 0:
                print(digit, stack[-1])
                stack.pop()
                print(stack)
                k -= 1
            stack.append(digit)
        
        result = int(''.join(stack))
        return str(result)
        