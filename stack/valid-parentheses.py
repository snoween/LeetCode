class Solution:
    def isValid(self, s: str) -> bool:
        brac_dict = {')': '(',
                     ']': '[',
                     '}': '{'}
        # stack
        # gap open bracket bo vo stack
        # khi gap close , check cai element cuoi cung cua cai stack xem co match hay ko
        stack = []
        for ele in s:
            if ele not in brac_dict:
                stack.append(ele)
            else:
                if not stack or brac_dict[ele] != stack[-1]:
                    return False
                stack.pop()
                
        return not stack