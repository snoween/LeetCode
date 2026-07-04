class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        unpair = 0

        for ele in s:
            if ele == '(':
                stack.append(ele)
            elif stack and ele == ')':
                stack.pop()
            elif not stack and ele == ')':
                unpair += 1
        
        return len(stack) + unpair