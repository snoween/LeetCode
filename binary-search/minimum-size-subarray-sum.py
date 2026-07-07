class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # First loop
        # total = 2 < 7 
        # Second loop
        # total = 5 < 7 
        # Third loop
        # total = 6 < 7 
        # Fourth loop
        # total = 8 > 7 --> length = right - left + 1 = 4
        # Increase left --> total = 3 + 1 + 2 = 6 
        # Fifth loop
        # total = 10 --> legth = 4
        total = 0
        min_length = inf

        left = 0
        for right, num in enumerate(nums):
            total += num

            while total >= target:
                min_length = min(min_length, right - left + 1)
                total = total - nums[left]
                left += 1
        
        return min_length if min_length != inf else 0
