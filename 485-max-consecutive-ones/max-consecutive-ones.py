class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Solution:
        1 1 0 1 1 1 -> first two ones, and last three ones -> return 3
        -> use 'ones' and 'max_ones' to count
        'ones': track the current count of consecutive 1s
        'max_ones': track the maximum count of 1s
        -> if see 0 -> re-count the 'ones', update 'max_ones'
        Time comp: O(N)
        Space comp: O(1)
        """
        ones = 0
        max_ones = 0

        for num in nums:
            if num == 1:
                ones += 1
            else:
                max_ones = max(max_ones, ones)
                ones = 0      

        return max(max_ones, ones)