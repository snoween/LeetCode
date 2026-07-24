class Solution:
    def longestPalindrome(self, s: str) -> int:
        # get the freq of all char
        freq = Counter(s)
        # set max_odd = 0
        max_odd = 0
        count_odd = 0
        # set max_len = 0
        sum_even = 0
        # loop through values of counter
        for val in freq.values():
            # if val is even:
            if val % 2 == 0:
                # max_len + val
                sum_even += val
            # if val is odd
            else:
                # update max odd
                count_odd += 1
                max_odd += val
                
        # return max len + max odd
        if count_odd == 0:
            return max_odd + sum_even

        return sum_even + max_odd - count_odd + 1