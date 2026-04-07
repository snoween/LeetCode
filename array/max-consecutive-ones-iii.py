class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count_0 = 0
        max_one = 0

        for r, num in enumerate(nums):
            if num == 0:
                count_0 += 1

            while count_0 > k:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1

            max_one = max(max_one, r-l+1)
        return max_one