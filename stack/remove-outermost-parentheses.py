class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        depth = 0
        
        for ele in s:
            if ele == '(':
                if depth > 0:
                    stack.append(ele)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    stack.append(ele)
        
        return ''.join(stack)