class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_min = [0] * n
        min_idx = inf

        for i in range(n):
            prefix_max[i] = max(prefix_max[i-1] if i > 0 else -inf, nums[i])
        
        for j in range(n-1, -1, -1):
            suffix_min[j] = min(suffix_min[j+1] if j < n-1 else inf, nums[j])
        
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                min_idx = min(min_idx, i)
        
        return min_idx if min_idx != inf else -1