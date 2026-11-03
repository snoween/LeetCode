class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        minNumber = float(inf)

        for i in range(0, len(nums) - 1, 2):
            curr = int(str(nums[i]) + str(nums[i + 1]))
            minNumber = min(minNumber, curr)

        return minNumber