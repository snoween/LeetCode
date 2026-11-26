class Solution:
    def rob(self, nums: list[int]) -> int:
        seen = {}

        def dp(i):
            if i < 0:
                return 0
            
            if i in seen:
                return seen[i]
            
            seen[i] = max(nums[i] + dp(i - 2), dp(i - 1))
            return seen[i]

        return dp(len(nums) - 1)