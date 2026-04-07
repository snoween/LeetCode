class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        nums_dict = Counter()
        max_one = 0

        for r, num in enumerate(nums):
            nums_dict[num] += 1
            while nums_dict[0] > k:
                if nums[l] == 0:
                    nums_dict[0] -= 1
                l += 1
            
            max_one = max(max_one, r-l+1)
        return max_one