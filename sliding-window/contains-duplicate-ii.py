class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        for r, num in enumerate(nums):
            while l < r and nums[l] == nums[r]:
                if r - l <= k:
                    return True
                else:
                    l = r
        
        return False 