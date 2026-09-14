class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solution: Find the starting number 
        - Starting number = Current number - 1
        - Update the length while curr_num + 1 in nums
        """
        set_nums = set(nums)
        max_len = 0

        # loop through nums
        for curr in set_nums:
            # check if curr is starting point
            if curr - 1 not in set_nums:
                start = curr
                curr_len = 0

                while start in set_nums:
                    curr_len += 1
                    start += 1
                    print(curr_len)
                # update max len
                max_len = max(max_len, curr_len)
        
        return max_len