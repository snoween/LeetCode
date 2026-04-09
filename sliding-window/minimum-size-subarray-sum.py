class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best_len = inf
        curr_sum = 0

        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_sum -= nums[l]
                best_len = min(best_len, r-l+1)
                l += 1
                
        return best_len if best_len != inf else 0