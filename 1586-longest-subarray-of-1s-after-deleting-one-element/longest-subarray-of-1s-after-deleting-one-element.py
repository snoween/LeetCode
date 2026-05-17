class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zero = 0
        max_len = 0
        l = 0

        for r, num in enumerate(nums):
            count_zero += int(num == 0)

            while count_zero > 1:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            
            max_len = max(max_len, r-l)
        
        return max_len