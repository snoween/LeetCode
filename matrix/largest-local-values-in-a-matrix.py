class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        new_grid = [[0] * (n - 2) for _ in range(n - 2)]

        DIRS = [(0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                curr = grid[i][j]

                for x, y in DIRS:
                    n_x = i + x
                    n_y = j + y
                    
                    if n_x < n and n_y < n:
                        curr = max(curr, grid[n_x][n_y])

                new_grid[i][j] = curr
        return new_grid