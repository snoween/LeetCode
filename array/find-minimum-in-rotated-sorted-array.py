class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Solution: Binary Search - rotated array, lower bound
        - Find breaking point
        - If nums[right] < nums[mid] -> left = middle + 1
        - If not, right = middle, half left has smaller num

        Time comp: O(logN)
        Space comp: O(1)
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            # Check if half right is sorted
            if nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle

        return nums[left] 