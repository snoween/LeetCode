class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        nums = [a, b, c]
        nums.sort()
        
        if nums[0] + nums[1] < nums[2]:
            return nums[1]

        return nums[2] - nums[0]
        