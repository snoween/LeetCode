class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_counter = Counter(s)
        l = 0
        char = 'A' if s_counter['A'] < s_counter['B'] else 'B'
        count = 0
        max_char = 0

        for r in range(len(s)):
            if s[r] == char:
                count += 1
            
            while count > k:
                if s[l] == char:
                    count -= 1
                l += 1
            
            max_char = max(max_char, r-l+1)
        
        return max_char