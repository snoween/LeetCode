class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Solution: check occurance
        Time comp: O(N)
        Space comp: O(1)
        """
        seenIndex = {}

        for i, num in enumerate(nums):
            if num in seenIndex and (i - seenIndex[num]) <= k:
                return True
            seenIndex[num] = i
        
        return False