class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        init_area = (r - l) * min(height[l], height[r])

        while l < r:
            area = (r - l) * min(height[l], height[r])
            
            if height[l] < height[r]:        
                l += 1
            
            else:
                r -= 1

            output = max(init_area, area)
            init_area = output
        
        return output