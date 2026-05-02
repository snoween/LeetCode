class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        start_val = 1
        pref = defaultdict(lambda: start_val)

        for i in range(n):
            pref[i] = pref[i-1] + nums[i] 
        
        del pref[-1]
        
        min_val = min(pref.values())
        if min_val < 1:
            start_val = start_val + abs(min_val) + 1
        
        return start_val