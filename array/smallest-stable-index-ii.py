class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = defaultdict(lambda: -inf)
        suffix_min = defaultdict(lambda: inf)
        output = [0] * n

        for i in range(n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        for j in range(n-1, -1, -1):
            suffix_min[j] = min(suffix_min[j+1], nums[j])
        

        for i in range(n):
            output[i] = prefix_max[i] - suffix_min[i]
            if output[i] <= k:
                return i

        return -1