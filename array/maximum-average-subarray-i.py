class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_val = sum(nums[:k])
        ans = window_val

        for r in range(k, len(nums)):
            window_val = window_val + nums[r] - nums[r-k]
            ans = max(ans, window_val)
        
        return ans / k