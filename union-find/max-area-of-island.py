class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        - Algorithm: BFS - no level 
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """
        row, col = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0
        visited = set()

        def getArea(x, y):
            area = 1    # (x, y) input is the first land
            # queue to store land boxes
            queue = deque()
            queue.append((x, y))
            visited.add((x, y))

            while queue:
                x, y = queue.popleft()

                # get neighbor values
                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]

                    # check if valid box and is land
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                        if (newX, newY) not in visited:
                            area += 1
                            queue.append((newX, newY))
                            visited.add((newX, newY))
                
            return area
        
        # loop through matrix, call function when that is land and not in visited
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1 and (x, y) not in visited:
                    max_area = max(max_area, getArea(x, y))
        
        return max_area
