class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        Algorithm: BFS - no layer
        Time com: O(N)
        Space comp: O(N)
        """
        row, col = len(grid), len(grid[0])
        # neighbors
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # set to store all visited computers
        visited = set()

        # function to get the number of computers connected 
        def numComputers(x: int, y: int) -> int:
            # stack to keep coor of computers
            stack = [(x, y)]
            visited.add((x, y))
            computers = 1

            while stack:
                curr_x, curr_y = stack.pop()

                for coor in DIRS:
                    newX = curr_x + coor[0]
                    newY = curr_y + coor[1]

                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                        if ((newX, newY)) not in visited:
                            stack.append((newX, newY))
                            visited.add((newX, newY))
                            computers += 1
                    
            return computers
        
        servers = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1 and (x, y) not in visited:
                    computers = numComputers(x, y)
                    if computers > 1:
                        servers += computers
        
        return servers
        
                