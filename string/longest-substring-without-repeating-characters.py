class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        max_length = 0
        
        left = 0
        for right, char in enumerate(s):
            seen[char] += 1
                
            while seen[char] > 1:
                seen[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
        return max_length     