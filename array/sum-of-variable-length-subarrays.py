class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        """
        Solution:
        - Calculate prefix sum
        - for each range, the value = prefix[end] - prefix[start - 1] if 
        start != 0, else value = prefix[end]
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        total = 0
        for i in range(n):
            start = max(0, i - nums[i])
            if start == 0:
                total += prefix[i]
            else:
                total += (prefix[i] - prefix[start - 1])
        
        return total