class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        unique_char = len(set(s))

        for i in range(1, unique_char+1):
            l = 0
            freq = {}
            char_k = 0

            for r, char in enumerate(s):
                if char not in freq:
                    freq[char] = 0

                freq[char] += 1
                if freq[char] == k:
                    char_k += 1

                while len(freq) > i:
                    if freq[s[l]] == k:
                        char_k -= 1

                    freq[s[l]] -= 1

                    if freq[s[l]] == 0:
                        del freq[s[l]]
                    l += 1
            
                if len(freq) == i and char_k == i:
                    max_len = max(max_len, r-l+1)

        return max_len

