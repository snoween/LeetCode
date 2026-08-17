class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        # neighbors
        DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


        # queue to save next step
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))


        seen_step = set()
        seen_step.add((entrance[0], entrance[1]))


        layer = 0
        while queue:
            x, y, step = queue.popleft()
            for coor in DIRS:
                newX = x + coor[0]
                newY = y + coor[1]


                if 0 <= newX < row and 0 <= newY < col and maze[newX][newY] == '.':
                    if (newX, newY) not in seen_step:
                        queue.append((newX, newY, step + 1))
                        seen_step.add((newX, newY))
                    
                    if (newX == 0 or newX == row - 1) or (newY == 0 or newY == col - 1):
                        return step + 1


        return -1
