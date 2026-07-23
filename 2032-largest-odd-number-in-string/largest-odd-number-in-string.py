class Solution:
    def largestOddNumber(self, num: str) -> str:
        # set init odd index = -1
        odd_idx = -1
        # loop through str
        for i, digit in enumerate(num):
            # if number is odd
            if int(digit) % 2 != 0:
                # update odd index
                odd_idx = i
        
        if odd_idx == -1:
            return ''
        else:
            return num[:odd_idx+1]
        # return string from 0 -> odd index if odd idx not -1, else empty str