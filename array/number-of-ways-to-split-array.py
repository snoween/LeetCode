class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        prefix = list(accumulate(nums))
        total = prefix[-1]
        
        for i in range(n-1):
            if prefix[i] >= total - prefix[i]:
                count += 1
        
        return count