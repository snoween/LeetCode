class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        col_ele = []
        
        # Check if grid[0] has different elements
        for i in range(n-1):
            if grid[0][i] != grid[0][i+1]:
                continue
            else:
                return False
            
        # Checl if each column of grid has all the same elements
        for i in range(n):
            for j in range(m-1):
                col_ele.append(grid[j][i]) if grid[j][i] == grid [j+1][i] else None
            if len(col_ele) != (m-1):
                return False
            else:
                col_ele = []

        return True    