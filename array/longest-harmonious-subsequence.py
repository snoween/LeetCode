class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # [1 2 2 2 3 3 5 7]
        # First loop
        # max = 1, min = 1 
        # Second loop
        # max = 2, min = 1 -> valid, length = 2
        # Third loop
        # max = 2, min = 1 -> valid, length = 3
        # Fourth loop
        # max = 2, min = 1 -> valid, length = 4
        #Fifth loop
        # max = 3, min = 1 -> invalid -> left + 1
        # max = 3, min = 2 -> valid, length = 4
        nums.sort()
        max_length = 0
        max_num = nums[0]
        min_num = nums[0]
        left = 0
        
        for right, num in enumerate(nums):
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
            
            while left < right and max_num - min_num > 1:
                left += 1
                min_num = nums[left]

            if max_num - min_num != 0:
                max_length = max(max_length, right - left + 1)
        
        return max_length 