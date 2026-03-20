class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        init_area = (r - l) * min(height[l], height[r])

        while l < r:
            if height[l] < height[r]:
                area = (r - l) * height[l]
                l += 1
            
            else:
                area = (r - l) * height[r]
                r -= 1

            output = max(init_area, area)
            init_area = output
        
        return output