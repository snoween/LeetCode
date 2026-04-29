class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [nums[0]] * n

        for i in range(1, n):
            output[i] = output[i-1] + nums[i]
        
        return output