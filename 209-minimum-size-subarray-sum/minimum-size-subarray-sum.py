class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = inf
        l = 0
        current_sum = 0

        for r, num in enumerate(nums):
            current_sum += num
            
            while current_sum >= target:
                current_sum -= nums[l]
                ans = min(ans, r-l+1)
                l += 1
        
        return ans if ans != inf else 0