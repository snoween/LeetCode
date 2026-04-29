class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = defaultdict(int)
        suffix = defaultdict(int)
        min_val = inf
        curr_val, best_idx = 0, 0

        for i in range(n):
            prefix[i] = prefix[i-1] + nums[i]
        
        for j in range(n-1, -1, -1):
            suffix[j] = suffix[j+1] + nums[j]
        
        for i in range(n):
            curr_val = abs((prefix[i] // (i+1)) - ((suffix[i+1] // (n-i-1)) if n-i > 1 else 0))
            if curr_val < min_val:
                min_val = curr_val
                best_idx = i

        return best_idx