class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        
        return result