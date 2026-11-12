class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_num = set(nums)
        max_len = 0

        for num in set_num:
            # find the starting number
            if num - 1 not in set_num:
                start = num
                curr_len = 0
                while start in set_num:
                    start += 1
                    curr_len += 1
            
                max_len = max(max_len, curr_len)
        
        return max_len