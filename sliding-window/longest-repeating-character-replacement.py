class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count_A = 0
        max_char = 0

        for r in range(len(s)):
            if s[r] == 'A':
                count_A += 1
            
            while count_A > k:
                if s[l] == 'A':
                    count_A -= 1
                l += 1
            
            max_char = max(max_char, r-l+1)
        
        return max_char
            
