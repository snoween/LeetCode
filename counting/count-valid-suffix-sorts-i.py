class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)
     
        P = 0
        while P < n and nums[P] == target[P]:
            P += 1
            
        S = n - 1
        while S > 0 and target[S - 1] >= target[S]:
            S -= 1

        if P < S:
            return 0
            
        max_valid_p = min(P, n - 1)
        
        if sorted(nums[max_valid_p:], reverse=True) == target[max_valid_p:]:
            return max_valid_p - S + 1
            
        return 0
