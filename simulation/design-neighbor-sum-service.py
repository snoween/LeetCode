class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.match = defaultdict(int)
        self.n = len(grid)
        for i in range(self.n):
            for j in range(self.n):
                self.match[grid[i][j]] = (i, j)
        
    def adjacentSum(self, value: int) -> int:
        DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        x, y = self.match[value]
        total = 0

        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < self.n and 0 <= ny < self.n):
                continue
            total += self.grid[nx][ny]
        
        return total

    def diagonalSum(self, value: int) -> int:
        DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        x, y = self.match[value]
        total = 0

        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < self.n and 0 <= ny < self.n):
                continue
            total += self.grid[nx][ny]
        
        return total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)