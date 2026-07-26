class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        # Set fresh = 0 to count fresh fruit later
        fresh = 0
        # Make rotten as deque to pop left later
        rotten = deque()
        
        # Get coordinates of rotten fruits, count fresh fruits
        for row in range(m):
            for col in range(n):
                # If ele = 2 -> append to rotten
                if grid[row][col] == 2:
                    rotten.append((row, col))
                # If ele = 1 -> fresh fruit + 1
                if grid[row][col] == 1:
                    fresh += 1

        # If no fresh fruits -> None
        if fresh == 0:
            return 0
        
        rotten_time = 0
        # Loop until no rotten fruits anymore
        while rotten:
            # Get size of CURRENT ROTTEN ARRAY
            size = len(rotten) 
            # Make default isrotten = False
            isRotten = False

            # Change neighbors to rotten fruits
            for _ in range(size):
                # Get coor of rotten
                rot_i, rot_j = rotten.popleft()

                # Get coor of neighbors by using DIRS
                for i, j in DIRS:
                    ni = i + rot_i
                    nj = j + rot_j

                    # If fresh fruit and row, col in range (m, n)
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        # Change fresh to rotten
                        grid[ni][nj] = 2  
                        # Fresh - 1  
                        fresh -= 1
                        # Append new rotten point
                        rotten.append((ni, nj))
                        # has rotten -> True
                        isRotten = True
                        
            # If isRotten
            if isRotten:
                # time + 1
                rotten_time += 1

        # If still has fresh fruits -> return -1
        if fresh != 0:
            return -1
            
        return rotten_time   