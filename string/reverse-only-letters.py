class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        li_s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if li_s[l].isalpha() and li_s[r].isalpha():
                li_s[l], li_s[r] = li_s[r], li_s[l]
                l += 1
                r -= 1
            
            elif not li_s[r].isalpha():
                r -= 1
            
            elif not li_s[l].isalpha():
                l += 1
        
        return ''.join(li_s)