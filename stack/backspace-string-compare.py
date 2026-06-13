class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checkstring(input_str):
            stack = []
            for ele in input_str:
                if ele != '#':
                    stack.append(ele)
                else:
                    if stack:
                        stack.pop()
            return stack
        
        return checkstring(s) == checkstring(t)