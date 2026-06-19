# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        result = 0

        while left <= right:
            middle = left + (right - left) // 2

            if isBadVersion(middle):
                result = middle
                right = middle - 1
            else:
                left = middle + 1

        return result