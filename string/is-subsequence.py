class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        li_s = list(s)
        li_t = list(t)
        i = 0

        if not s:
            return True

        for j, char in enumerate(li_t):
            if char == li_s[i] and i < len(s) - 1:
                i += 1
            
            if j == len(li_t) - 1 and i < len(li_s) - 1:
                return False
        
        return True

            


