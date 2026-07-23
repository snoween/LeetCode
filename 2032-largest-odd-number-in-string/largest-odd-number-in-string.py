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
        
        # Check if odd idx = -1
        if odd_idx == -1:
            # it means no odd number -> return empty str
            return ''
        # if not -1, return str from 0 -> odd idx + 1
        return num[:odd_idx+1]