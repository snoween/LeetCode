class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxLength = 0
        countZero = 0

        left = 0
        for right, num in enumerate(nums):
            countZero += int(num == 0)

            while countZero > k:
                countZero -= int(nums[left] == 0)
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength