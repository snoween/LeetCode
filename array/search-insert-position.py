class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Solution: Binary Search - lower bound
        - If nums[middle] = target -> return
        - Else -> shrink the range: 
            - if num[mid] > target: -> right = mid, left += 1
            -> return left
        """
        left, right = 0, len(nums)

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                right = middle
            else:
                left += 1
            
        return left