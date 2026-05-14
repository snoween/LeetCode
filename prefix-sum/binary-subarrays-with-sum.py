class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        curr_sum = 0
        count = 0
        zero = 0
        for r, num in enumerate(nums):
            curr_sum += num
            while l < r and (curr_sum > goal or nums[l] == 0):
                if nums[l] == 0:
                    zero += 1
                else:
                    zero = 0
                curr_sum -= nums[l]
                l += 1

            if curr_sum == goal:
                count += zero + 1
        
        return count