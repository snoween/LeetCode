class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_val = sum(nums[:k])      # Init window
        ans = window_val        # Init answer

        for r in range(k, len(nums)):
            window_val = window_val + nums[r] - nums[r-k]   # Shift to right, fixed size
            ans = max(ans, window_val)      # Update max window sum
        
        return ans / k