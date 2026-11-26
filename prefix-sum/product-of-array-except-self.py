class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        - Prefix product
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # calculate prefix
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # calculate suffix
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        return [prefix[k] * suffix[k] for k in range(n)]