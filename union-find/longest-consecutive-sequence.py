class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Brute force
        If num - 1 not in set_nums
            start = num
            keep looking up start += 1 in set_nums -> update count
            update longest seq
        Time comp: O(N)
        Space comp: O(N)
        """

        set_nums = set(nums)
        longest_seq = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                start = num
                length = 0
                while start in set_nums:
                    start += 1
                    length += 1

                longest_seq = max(longest_seq, length)
        
        return longest_seq