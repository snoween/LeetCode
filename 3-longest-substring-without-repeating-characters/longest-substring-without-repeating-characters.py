class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char = set()
        ans = 0
        l = 0

        for r, char in enumerate(s):
            while char in seen_char:
                seen_char.remove(s[l])
                l += 1
            
            seen_char.add(char)

            ans = max(ans, r-l+1)
        
        return ans