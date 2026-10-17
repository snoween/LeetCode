class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Solution: Sliding window
        Window with min length - has sum >= target
        -> Expand the window when window sum < target
        -> Shrink when window sum > target

        Time comp: O(N)
        Space comp: O(1)
        """

        currentSum = 0
        minLength = float(inf)

        left = 0
        for right, num in enumerate(nums):
            currentSum += num
            while currentSum >= target:
                minLength = min(minLength, right - left + 1)
                currentSum -= nums[left]
                left += 1      
        
        return minLength if minLength != float(inf) else 0