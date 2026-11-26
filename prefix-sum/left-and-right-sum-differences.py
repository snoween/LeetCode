class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """
        Solution: prefix sum/suffix sum
        - ans[i] = abs(suffix[i] - prefix[i])
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        suffix = [0] * n
        suffix[-1] = nums[-1]
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] + nums[j]
        
        return [abs(prefix[i] - suffix[i]) for i in range(n)]
