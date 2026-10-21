class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Solution: Binary search
        - Find the breaking point
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle
        
        return nums[left]
