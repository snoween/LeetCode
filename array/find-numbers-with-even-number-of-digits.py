import math
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            digits = int(math.log10(num)) + 1
            if digits % 2 ==  0:
                count += 1

        return count

        