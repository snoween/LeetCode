class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        prefix = list(accumulate(nums))
        total = prefix[-1]
        
        for i in range(n-1):
            count += int(prefix[i] >= total - prefix[i])
        
        return count