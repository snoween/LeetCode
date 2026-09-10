class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - Algorithm: multi starting points - BFS, traversal by level
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """
        m, n = len(grid), len(grid[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        # Step 1: Get all sources, visited and count fresh oranges
        sources = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    sources.append((r, c))

        # Edge case: check if any fresh oranges 
        if fresh == 0:
            return 0

        # Step 2: BFS by layer
        time = 0

        while sources:
            time += 1
            length = len(sources)

            for _ in range(length):
                currX, currY = sources.popleft()

                # loop 4 dir adj
                for x, y in DIRS:
                    newX = x + currX
                    newY = y + currY

                    # check if neighbor is valid
                    if not (0 <= newX < m and 0 <= newY < n):
                        continue
                    
                    if grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        sources.append((newX, newY))

                        fresh -= 1
                        if fresh == 0:
                            return time
        
        return -1
