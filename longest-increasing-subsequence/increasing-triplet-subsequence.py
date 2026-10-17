class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        x, y = float("INF"), float("INF")

        # Try to find the 2 smallest numbers
        for num in nums:
            if num <= x:
                x = num
            elif num <= y:
                y = num
            else:   
                return True     # Already has x, y. Return True if any num > x & y
        
        return False