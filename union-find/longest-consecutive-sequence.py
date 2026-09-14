class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solution: Find the starting number 
        - Starting number = Current number - 1
        - Update the length while curr_num + 1 in nums
        """
        nums_set = set(nums)
        max_len = 0

        for num in nums:
            # if starting num not in nums_set -> curr = starting
            if num - 1 not in nums_set:
                init_num = num
                curr_len = 1

                while init_num + 1 in nums_set:
                    init_num += 1
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len