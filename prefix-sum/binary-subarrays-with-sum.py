class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Solution: count subarray if its sum = goal
        Time comp: O(N)
        Space comp: O(1)
        goal = 2
        [0 0 1 1 0 0] -> count = 9
        [0 0 1 1]
        [0 1 1]
        [1 1]
        -> 2 left zeros = 3 valid arrays
        """
        valid = 0
        currentSum = 0
        leftZeros = 0

        left = 0
        for right, num in enumerate(nums):
            currentSum += num

            while left < right and (currentSum > goal or nums[left] == 0):
                if nums[left] == 0:
                    leftZeros += 1
                else:
                    leftZeros = 0
                currentSum -= nums[left]
                left += 1
            
            if currentSum == goal:
                valid += leftZeros + 1
        
        return valid