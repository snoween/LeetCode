class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = Counter()
        best_len = 0
        l = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            while len(seen) > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1

            best_len = max(best_len, r-l+1)

        return best_len