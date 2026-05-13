class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        l = 0
        min_len = inf

        for i, num in enumerate(nums):
            curr_sum += num

            while curr_sum >= target:
                min_len = min(min_len, i-l+1)
                curr_sum -= nums[l]
                l += 1
        
        return min_len if min_len != inf else 0