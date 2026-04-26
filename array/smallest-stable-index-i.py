class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        min_idx = inf
        for i in range(1, len(nums)):
            max_num = max(nums[:i])
            min_num = min(nums[i:])
            
            if max_num - min_num <= k:
                min_idx = min(min_idx, i)
        
        return min_idx if min_idx != inf else -1