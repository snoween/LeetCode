class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - Algorithm: BFS - stack
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """
        row, col = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]   # Neighbor coordinates

        numIslands = 0
        visited = set()

        def isIsland(x: int, y: int):
            # queue to store lands
            stack = [(x, y)]
            visited.add((x, y))

            while stack:
                x, y = stack.pop()
                # get neighbor values
                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]

                    # check if valid land 
                    if not (0 <= newX < row and 0 <= newY < col):
                        continue
                    if grid[newX][newY] == '1' and (newX, newY) not in visited:
                        stack.append((newX, newY))
                        visited.add((newX, newY))
        

        # loop through grid to get all number of islands
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x, y) not in visited:
                    isIsland(x, y)
                    numIslands += 1
        
        return numIslands 
