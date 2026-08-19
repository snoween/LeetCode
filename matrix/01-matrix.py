class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        - Algorithm: BFS - multi sources
        - Time comp: O(M x N)
        - Space: O(M x N)
        - Note: no need 'visited' because all values in queue are unique
        """

        # Edge case: check if valid 2D matrix or not
        if not mat or not mat[0]:
            return []
        
        row, col = len(mat), len(mat[0])
        # use queue to store all sources (node = 0)
        queue = deque()
        # create a matrix distance to store distance between 1-0, default = -1
        dist = [[-1] * col for _ in range(row)]
        # loop through mat to get coors of all sources (node = 0), dist at source = 0
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    dist[r][c] = 0
        
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # loop while valid queue
        while queue:
            x, y = queue.popleft()      # get coor of current box
            # get neighbor values
            for coor in DIRS:
                newX = x + coor[0]
                newY = y + coor[1]
                # check if valid neighbor coor and value = -1
                if 0 <= newX < row and 0 <= newY < col and dist[newX][newY] == -1:
                    # update new distance for neighbor value
                    dist[newX][newY] = dist[x][y] + 1
                    queue.append((newX, newY))
        
        return dist
