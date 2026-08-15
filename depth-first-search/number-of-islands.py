class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        numIslands = 0
        seen = set()

        def ifIsland(curr_row: int, curr_col:int) -> int:
            queue = deque()
            queue.append((curr_row, curr_col))
            seen.add((curr_row, curr_col))

            while queue:
                x, y = queue.popleft()

                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]
                    print(newX, newY)
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                        print(newX, newY)
                        if (newX, newY) not in seen:
                            seen.add((newX, newY))
                            queue.append((newX, newY))
            
        for curr_row in range(row):
            for curr_col in range(col):
                if grid[curr_row][curr_col] == 1 and (curr_row, curr_col) not in seen:
                    numIslands += 1
                    print(seen)
                    ifIsland(curr_row, curr_col)
        
        return numIslands