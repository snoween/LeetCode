class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i, num in enumerate(nums):
            first_num = num
            k = i + 1
            while k < len(nums):
                if nums[k] == first_num:
                    count += 1
                k += 1
        
        return count