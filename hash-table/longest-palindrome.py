class Solution:
    def longestPalindrome(self, s: str) -> int:
        # get the freq of all char
        freq = Counter(s)
        # set count_odd = 0
        count_odd = 0
        # set max_len = 0
        max_len = 0

        # loop through values of counter
        for val in freq.values():
            # if val is odd:
            if val % 2 != 0:
                # update count odd
                count_odd += 1
            # update max len
            max_len += val
                
        # return max len + max odd
        if count_odd == 0:
            return max_len

        return max_len - count_odd + 1