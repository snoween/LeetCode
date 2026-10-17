class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Solution: Prefix product
        Time: O(N)
        Space: O(N)
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        return [prefix[i] * suffix[i] for i in range(n)]
