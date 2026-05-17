class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_dict = defaultdict(int)

        for i, num in enumerate(nums):
            if num not in idx_dict:
                idx_dict[num] = i
            
            else:
                if i - idx_dict[num] <= k:
                    return True
                else:
                    idx_dict[num] = i
        
        return False