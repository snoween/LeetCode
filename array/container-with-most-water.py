class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        first_area = (r - l) * min(height[l], height[r])
        area = []
        area.append(first_area)
        
        while l < r:
            if height[l] < height[r]:
                new_area = (r - l) * min(height[l], height[r])
                l += 1
            
            if height[l] >= height[r]:
                new_area = (r - l) * min(height[l], height[r])
                r -= 1

            area.append(new_area)
        
        return max(area)