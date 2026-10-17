class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        curr_len = 0
        max_len = 0

        for num in arr:
            if num % 2 != 0:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0
        
        return max_len >= 3