class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        DIRS = ([-1, -1], [-1, 0], [-1, 1],
                [0, -1], [0, 1],
                [1, -1], [1, 0], [1, 1])
        
        if grid[0][0] == 1:
            return -1
        
        queue = deque()
        queue.append((0, 0))
        seen = set()

        len_path = 1

        while queue:
            n = len(queue)
            len_path += 1
            for _ in range(n):
                x, y = queue.popleft()
                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]
                    print(newX, newY)
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 0:
                        if (newX, newY) not in seen:
                            seen.add((newX, newY))
                            queue.append((newX, newY))

                        if newX == row - 1 and newY == col - 1:
                            return len_path

        return -1