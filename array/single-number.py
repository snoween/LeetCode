class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)
        
        for key, value in nums_dict.items():
            if value == 1:
                return key