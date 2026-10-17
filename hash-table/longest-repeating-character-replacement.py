class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        max_len = 0

        left = 0
        for right, char in enumerate(s):
            freq[char] += 1

            while (right-left+1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len