class Solution:
    def isValid(self, s: str) -> bool:
        brac_pairs = {'}': '{',
                    ')': '(',
                    ']': '['}
        open_brac = []

        for ele in s:
            if ele not in brac_pairs:
                open_brac.append(ele)
            else:
                if open_brac and brac_pairs[ele] == open_brac[-1]:
                    open_brac.pop()
                else:
                    return False
        
        return True
