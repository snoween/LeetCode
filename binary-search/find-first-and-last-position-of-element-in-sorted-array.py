class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Solution: Binary search
        - Find lower bound + upper bound
        """

        def lowerBound(arr, target):
            left, right = 0, len(arr)
            while left < right:
                middle = left + (right - left) // 2
                if arr[middle] >= target:
                    right = middle
                else:
                    left = middle + 1
            return left 
        
        def upperBound(arr, target):
            left, right = 0, len(arr)
            while left < right:
                middle = left + (right - left) // 2
                if arr[middle] > target:
                    right = middle
                else:
                    left = middle + 1
            return left
        
        left = lowerBound(nums, target)
        right = upperBound(nums, target)
    
        return [left, right - 1] if left < right else [-1, -1]