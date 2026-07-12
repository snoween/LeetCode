class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # [0 3 2 1]
        # loop 0: 
        # nums[0] = 0 -> ok
        # loop 1:
        # nums[1] = 3 -> take -1 & 3 = 3 -> ans = 3
        # loop 2:
        # nums[2] = 2 -> ok
        # loop 3:
        # nums[3] = 1 -> 3 & 1 = 1 -> ans = 1

        ans = -1 
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
        return max(ans, 0) # 0 if sorted input