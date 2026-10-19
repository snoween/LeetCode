class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Solution: Binary search
        Time comp: O(logN)
        Space comp: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1