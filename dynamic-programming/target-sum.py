class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        path_val = 0
        
        @lru_cache(None)
        def backtrack(path_val, index):
            if index == len(nums):
                return int(path_val == target)
            
            add_way = backtrack(path_val + nums[index], index + 1)
            sub_way = backtrack(path_val - nums[index], index + 1)
            
            return add_way + sub_way

        return backtrack(0, 0)