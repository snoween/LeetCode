class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        freq = Counter(nums)
        middle = len(nums) // 2
        if freq[nums[middle]] == 1:
            return True
        return False