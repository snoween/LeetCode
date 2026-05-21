class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = Counter()
        max_len = 0

        left = 0
        for right, char in enumerate(s):
            freq[char] += 1

            while freq[char] > 1:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len