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
            heapq.heapify(stack)
            for row in range(m):
                heapq.heappush(stack, -grid[row][col])
                
            ans += heapq.heappop(stack)
        
        return -ans
            
            
                
        
