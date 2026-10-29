class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Solution: Sliding window, check frequency
        Shrink the window when frequency of that char > 1
        """
        freq = defaultdict(int)
        maxLength = 0

        left = 0
        for right, char in enumerate(s):
            freq[char] += 1

            while freq[char] > 1:
                freq[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength