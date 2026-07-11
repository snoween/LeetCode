class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # [[1,2,4],[3,3,1]]
        # First loop:
        # ans = 4 (4 > 3)
        # Second loop:
        # ans = 4 + 3 (2 < 3)
        # Third loop:
        # ans = 7 + 1 (1 = 1)

        m, n = len(grid), len(grid[0])
        ans = 0
        for arr in grid:
            arr.sort()
        
        for col in range(n - 1, -1, -1):
            stack = []
            for row in range(m):
                if stack and grid[row][col] > stack[-1]:
                    stack.pop()
                    stack.append(grid[row][col])
                elif not stack:
                    stack.append(grid[row][col])

            ans += stack[0]
        
        return ans
            
            
                
        
