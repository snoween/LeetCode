class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)

        if colors[0] != colors[-1]:
            return n - 1
        
        left = 0
        while colors[left] == colors[-1]:
            left += 1
        
        right = n - 1
        while colors[right] == colors[0]:
            right -= 1
        
        return max(right, n - 1 - left)