class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zero = 0
        max_len = 0

        left = 0
        for right, num in enumerate(nums):
            count_zero += int(num == 0)

            while count_zero > 1:
                count_zero -= int(nums[left] == 0)
                left += 1
            
            max_len = max(max_len, right-left)
        
        return max_len