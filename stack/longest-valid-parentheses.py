class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count_valid = 0

        for char in s:
            if char == '(':
                stack.append(char)
            elif stack and char == ')':
                stack.pop()
                count_valid += 1
        
        return count_valid*2