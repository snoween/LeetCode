class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge case
        if not s:
            return True
        
        k = 0
        for char in t:
            if k < len(s) and char == s[k]:
                k += 1
        
        return k == len(s)