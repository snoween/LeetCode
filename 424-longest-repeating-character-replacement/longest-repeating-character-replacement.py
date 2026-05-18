class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq = defaultdict(int)
        max_freq = 0
        l = 0

        for r, char in enumerate(s):
            freq[char] += 1
            max_freq = max(max_freq, freq[char])
            
            while (r-l+1) - max_freq > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len

                