class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best_len = inf
        l = 0
        current_sum = 0

        for r, num in enumerate(nums):
            current_sum += num

            while current_sum >= target:
                current_sum -= nums[l]
                best_len = min(best_len, (r - l + 1))
                l += 1
        
        return best_len if best_len != inf else 0