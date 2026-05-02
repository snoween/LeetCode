class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        start_val = abs(min(nums)) 
        pref = defaultdict(lambda: start_val)


        for i in range(n):
            pref[i] = pref[i-1] + nums[i] 
        
        del pref[-1]
        if min(pref.values()) < 1:
            start_val = abs(start_val) + abs(min(pref.values())) + 1
        
        return start_val