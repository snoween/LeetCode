class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Solution: Binary search, rotated array
        Time comp: O(logN), worst case is O(N)
        Space comp: O(1)
        - Check if target in half left or half right of the array
        - Because the numbers are not distinct, so we cannot shrink the range by using middle value. We have to move left/right by 1 unit (left += 1, right -= 1) to not miss any number (eg: 1 0 1 1 1)
        - Other steps will be done by using normal rotated binary search technique
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return True

            # Check if half left is sorted
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right -= 1
                else:
                    left += 1
            else:
                if nums[middle] < target <= nums[right]:
                    left += 1
                else:
                    right -= 1
        
        return False