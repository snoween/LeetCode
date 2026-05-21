class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0

        left = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(char)
            max_len = max(max_len, right-left+1)
        
        return max_len