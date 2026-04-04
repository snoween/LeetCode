class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        freq_p = Counter(p)
        freq = Counter(s[:k])
        ans = [0] if freq_p == freq else []

        for right in range(k, n):
            freq[s[right]] += 1
            freq[s[right - k]] -= 1

            if freq == freq_p:
                ans.append(right-k+1)

        return ans
