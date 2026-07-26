class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
   
        m, n = len(grid), len(grid[0])
        
        fresh = 0
        rotten = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        rotten_time = 0
        while rotten:
            size = len(rotten) 
            isRotten = False

            for i in range(size):
                rot_i, rot_j = rotten.popleft()
                for i, j in DIRS:
                    ni = i + rot_i
                    nj = j + rot_j

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        rotten.append((ni, nj))
                        isRotten = True
            
            if isRotten:
                rotten_time += 1

        if fresh != 0:
            return -1
            
        return rotten_time   