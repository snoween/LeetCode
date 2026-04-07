class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count_0 = 0
        count_num = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count_0 += 1

            while count_0 > k:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1

            count_num = max(count_num, r-l+1)
        return count_num