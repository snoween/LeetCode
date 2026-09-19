class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        list_nums = []
        def backtrack():
            if len(list_nums) == len(nums):
                result.append(list_nums[:])
                return
            
            for num in nums:
                if num not in list_nums:
                    list_nums.append(num)
                    backtrack()
                    list_nums.pop()
        
        backtrack()
        return result