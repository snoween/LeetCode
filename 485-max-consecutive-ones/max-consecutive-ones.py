class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        left = 0
        # loop through nums
        for right, num in enumerate(nums):
            if num == 0:
                count += 1
                while count > 0:
                    if nums[left] == 0:
                        count -= 1
                    left += 1

            max_count = max(max_count, right - left + 1)
        # return max count
        return max_count