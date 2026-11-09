class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        target = len(nums) // 2
        freq = Counter(nums)

        for key, val in freq.items():
            if val == target:
                return key