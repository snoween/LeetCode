class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        n = len(grid)        
        # Check if 2 neighbors are same type
        DIRS = [(0,0), (0,1), (1,0), (1,1)]

        for i in range(n-1):
            for j in range(n-1):
                count_B = 0

                for di, dj in DIRS:
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < n and 0 <= nj < n):
                        continue
                    
                    # Check if both hor + ver have same values
                    if grid[ni][nj] == 'B':
                        count_B += 1

                if count_B != 2:
                    return True
    
        return False