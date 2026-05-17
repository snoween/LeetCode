class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        unique_char = len(set(s))

        for i in range(1, unique_char + 1):
            freq = {}
            char_with_k = 0
            l = 0

            for r, char in enumerate(s):
                # Update dict freq
                if char not in freq:
                    freq[char] = 0
                freq[char] += 1

                # Count the number of char with appearing at least 'k' times
                if freq[char] == k:
                    char_with_k += 1
                
                # Shrink the array when has more than i diff chars
                while len(freq) > i:
                    if freq[s[l]] == k:
                        char_with_k -= 1
                    
                    freq[s[l]] -= 1

                    if freq[s[l]] == 0:
                        del freq[s[l]]
                    
                    l += 1
                
                # Update max len: meet 2 conditions
                if len(freq) == i and char_with_k == i:
                    max_len = max(max_len, r-l+1)
        
        return max_len