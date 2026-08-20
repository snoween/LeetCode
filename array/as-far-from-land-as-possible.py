class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        - Algorithm: BFS - multi sources 
        - Time comp: O(M x N)
        - Comp space: O(M x N)
        """
        rows, cols = len(grid), len(grid[0])
        # queue to store sources = land coors
        queue = deque()
        dist = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        if not queue or len(queue) == (rows * cols):
            return -1

        maxDist = 0
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            # get neighbors
            for dx, dy in DIRS:
                newX = x + dx
                newY = y + dy
                
                if not (0 <= newX < rows and 0 <= newY < cols):
                    continue
                if dist[newX][newY] != -1:
                    continue

                # update neighbor distance
                dist[newX][newY] = dist[x][y] + 1
                maxDist = max(maxDist, dist[newX][newY])
                queue.append((newX, newY))
        
        return maxDist