class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int)

        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = i
            
            else:
                if i - freq[num] <= k:
                    return True
                else:
                    freq[num] = i
        
        return False

        