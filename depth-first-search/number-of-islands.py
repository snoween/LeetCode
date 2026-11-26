class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Solution: BFS
        - Check if the 4-directional neighbors are 1 until no more in queue -> 1 island
        - Use set to mark visited cells
        - Loop through all not visited cells in grid if cell value = 1
        """
        rows, cols = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        
        def isIsland(r, c):
            visited.add((r, c))
            stack = [(r, c)]

            while stack:
                x, y = stack.pop()

                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in visited:
                        continue
                    if not (0 <= nx < rows and 0 <= ny < cols):
                        continue
                    
                    if grid[nx][ny] == '1':
                        stack.append((nx, ny))
                        visited.add((nx, ny))
            
            return 1
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += isIsland(r, c)
        
        return count