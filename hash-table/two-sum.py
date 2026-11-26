class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        - Check if the difference between target and nums[i] in dict or not
        """
        seen = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [i, seen[diff]]
            seen[num] = i
