class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        max_area = 0

        def ifIsland(curr_row: int, curr_col:int) -> int:
            queue = deque()
            queue.append((curr_row, curr_col))
            seen.add((curr_row, curr_col))
            area = 1

            while queue:
                x, y = queue.popleft()
                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]

                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                        if (newX, newY) not in seen:
                            seen.add((newX, newY))
                            queue.append((newX, newY))
                            area += 1
            
            return area
           
           
        for curr_row in range(row):
            for curr_col in range(col):
                if grid[curr_row][curr_col] == 1 and (curr_row, curr_col) not in seen:
                    area = ifIsland(curr_row, curr_col)
                    max_area = max(max_area, area)
        
        return max_area