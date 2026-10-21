class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Solution: Binary search, rotated array
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            # check if half left is sorted
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # half right is sorted
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1