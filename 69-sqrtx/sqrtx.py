class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Solution: binary search, upper bound
        """
        # edge case
        if x < 2:
            return x

        left, right = 1, x
        ans = 0
        while left < right:
            middle = left + (right - left) // 2

            # check if middle ^ 2 == x
            if middle != 0 and middle == x // middle:
                return middle
            elif middle != 0 and middle > x // middle:
                right = middle
            else:
                ans = middle
                left = middle + 1
        
        return ans