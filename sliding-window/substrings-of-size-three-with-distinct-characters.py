class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        curr_s = s[:3]
        count = int(len(set(curr_s)) == 3)

        for r in range(3, len(s)):
            curr_s = curr_s[1:] + s[r]
            count += int(len(set(curr_s)) == 3)
        
        return count