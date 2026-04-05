class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        
        freq_p = Counter(p)
        freq_s = Counter(s[:n])

        ans = [0] if freq_p == freq_s else []

        for r in range(n, m):
            freq_s[s[r]] += 1       # Update right edge
            freq_s[s[r - n]] -= 1   # Remove left edge

            if freq_s == freq_p:
                ans.append(r - n + 1)
        
        return ans