class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_idx = {i: i for i in range(n)}
        nums.sort()

        for i, num in enumerate(nums):
            if i != num:
                return i
        
        return n