class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        target = len(nums) / 2
        
        for key, val in freq.items():
            if val > target:
                return key