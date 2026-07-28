class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Pattern: 2 pointers same way
        # Make a counter to store unique char
        freq = Counter()
        # set init max_len = 0
        max_len = 0
        # left pointer = 0
        left = 0
        # loop through s
        for right, char in enumerate(s):
            # add freq of char in s
            freq[char] += 1
            # while char val > 1:
            while freq[char] > 1:
                # decrease left pointer val
                freq[s[left]] -= 1
                # left + 1
                left += 1
                
            # update max len = max(max_len, right - left + 1)
            max_len = max(max_len, right - left + 1)

        # return max_len
        return max_len