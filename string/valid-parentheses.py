class Solution:
    def isValid(self, s: str) -> bool:
        brac_pairs = {'}': '{',
                    ')': '(',
                    ']': '['}
        stack = []

        for ele in s:
            if ele not in brac_pairs:
                stack.append(ele)
            else:
                if not stack or brac_pairs[ele] != stack[-1]:
                    return False
                stack.pop()

        return not stack