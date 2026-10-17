class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []
        path = []

        def backtrack(index):
            result.append(path[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return result