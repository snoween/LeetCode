class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        """
        solution: brute force
        total = left sum + nums[i] + right sum
        left sum = right sum
        -> total = 2 * left sum + nums[i]
        -> nums[i] = total - 2 * left sum
        so if nums[i] = total - 2 * left sum -> return i
        """
        left_sum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            if num == total - 2 * left_sum:
                return i
            
            left_sum += num
        
        return -1