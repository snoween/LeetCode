class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        """
        - unique values -> if any nums appear more than once -> return
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)