class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_nums = set(nums)
        set_target = set([i for i in range(1, n+1)])
        
        return list(set_target - set_nums)