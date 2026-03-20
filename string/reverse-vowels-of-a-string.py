class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = 'ueoaiUEOAI'

        l, r = 0, len(s) - 1
        li_s = list(s)

        while l < r:
            if li_s[r] in VOWELS and li_s[l] in VOWELS:
                li_s[r], li_s[l] = li_s[l], li_s[r]
                l += 1
                r -= 1
            
            elif li_s[r] not in VOWELS:
                r -= 1
            
            elif li_s[l] not in VOWELS:
                l += 1
            
        return ''.join(li_s)