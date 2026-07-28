class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Pattern: 2 pointers same way
        # Make a set to store unique char
        freq = set()
        # set init max_len = 0
        max_len = 0
        # left pointer = 0
        left = 0
        # loop through s
        for right, char in enumerate(s):
            # while char right in set:
            while left < len(s) and s[right] in freq:
                # decrease left pointer val
                freq.remove(s[left])
                # left + 1
                left += 1
                
            # add freq of char in s
            freq.add(char)   
            # update max len = max(max_len, right - left + 1)
            max_len = max(max_len, right - left + 1)

        # return max_len
        return max_len