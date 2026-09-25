class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()
            
        backtrack()
        return result