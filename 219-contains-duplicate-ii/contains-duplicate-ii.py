class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int)
        
        for right, num in enumerate(nums):
            if num in freq:
                if right - freq[num] <= k:
                    return True
                else:
                    freq[num] = right
                    
            freq[num] = right
        
        return False