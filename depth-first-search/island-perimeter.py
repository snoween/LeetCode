class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        row, col = len(grid), len(grid[0])
        perimeter = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    neighbors = 0

                    for coor in directions:
                        ni = r + coor[0]
                        nj = c + coor[1]
                        if 0 <= ni < row and 0 <= nj < col:
                            neighbors += grid[ni][nj]
                    
                    perimeter += (4 - neighbors)
        
        return perimeter