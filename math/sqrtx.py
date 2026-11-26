class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Solution: binary search, upper bound
        """
        # edge case
        if x < 2:
            return x

        left, right = 1, x
        while left < right:
            middle = left + (right - left + 1) // 2     # plus 1 to round up

            if middle > x // middle:
                right = middle - 1
            else:
                left = middle 

        return left