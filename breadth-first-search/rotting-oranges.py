class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - Algorithm: multi starting points - BFS, tranversal by level
        - Time comp: O(M x N)
        - Space comp: O(M x N)
        """

        row, col = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # queue to store all rotten oranges at first
        queue = deque()

        # a parameter to count fresh oranges
        fresh = 0

        # loop through matrix to get all the rotten and fresh one
        for m in range(row):
            for n in range(col):
                if grid[m][n] == 2:
                    queue.append((m, n))
                    
                elif grid[m][n] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        # set init time
        time = 0

        while queue:
            time += 1
            len_queue = len(queue)
            # loop through all rotten oranges in queue now
            for _ in range(len_queue):
                x, y = queue.popleft()      #coor of current rotten one

                # loop to get neighbors values
                for coor in DIRS:
                    newX = x + coor[0]
                    newY = y + coor[1]

                    # if neighbor is fresh -> change to rotten, decrease fresh by 1
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        fresh -= 1
                        queue.append((newX, newY))

                        # if no fresh oranges -> return time
                        if fresh == 0:
                            return time

        return -1
