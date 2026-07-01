class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        stack = []
        for digit in num:
            while len(stack) > 0 and digit < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"
        