class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        for i in range(n):
            for j, ele in enumerate(grid[i]):
                # Check diagonals
                if (j == i or j == n-i-1) and ele == 0:
                    return False
                
                # Check other elements
                if (i != j and j != n-1-i) and ele != 0:
                    return False
        
        return True