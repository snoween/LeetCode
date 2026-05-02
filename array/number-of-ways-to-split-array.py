class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            prefix[i] = (prefix[i-1] if i > 0 else 0) + nums[i]
        
        for j in range(n-1, -1, -1):
            suffix[j] = (suffix[j+1] if j < n-1 else 0) + nums[j]
        
        for i in range(n-1):
            if prefix[i] >= suffix[i+1]:
                count += 1
        
        return count