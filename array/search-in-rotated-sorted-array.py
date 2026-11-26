class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Solution: binary search, rotated array
        Time comp: O(logN)
        Space comp: O(1)
        - Check if target is in half left or half right of the array
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            # Check if half left is sorted
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # else, half right is sorted
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1