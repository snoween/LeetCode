class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        nums = set(num for num in range(left, right + 1))
        for pair in ranges:
            x, y = pair
            for num in range(x, y + 1):
                if num in nums:
                    nums.remove(num)
        
        return not nums