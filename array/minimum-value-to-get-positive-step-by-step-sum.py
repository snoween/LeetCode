class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        start_val = 1
        pref = [1] * n

        for i in range(n):
            pref[i] = (pref[i-1] if i > 0 else 1) + nums[i] 

        print(pref)
        min_val = min(pref)
        if min_val < 1:
            start_val = abs(start_val) + abs(min_val) + 1
        
        return start_val