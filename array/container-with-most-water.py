class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
        
        return max_area