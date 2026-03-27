class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i, num in enumerate(nums):
            k = i + 1
            
            while k < len(nums):
                if nums[k] == num:
                    count += 1
                k += 1
        
        return count